import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px
import json
import utils.bggFetcher as bf
import xml.etree.ElementTree as ET


##########
import requests
from bs4 import BeautifulSoup
import re
from typing import List, Dict, Optional
from functools import lru_cache
class BGGFetcher:
    def __init__(self):
        self.base_url = "https://boardgamegeek.com/xmlapi2"
        if 'bgg_cache' not in st.session_state:
            st.session_state.bgg_cache = {}

    @staticmethod
    @st.cache_data(ttl=3600, show_spinner=False)
    def _fetch_api(endpoint: str, params: Dict) -> Optional[str]:
        """Generic API fetcher with retry logic"""
        try:
            base_url = "https://boardgamegeek.com/xmlapi2"
            url = f"{base_url}/{endpoint}"
            response = requests.get(url, params=params)
            
            # BGG sometimes returns 202 when preparing data
            if response.status_code == 202:
                time.sleep(2)  # Wait and retry
                response = requests.get(url, params=params)
            
            if response.status_code == 200:
                return response.content
            else:
                st.warning(f"Failed to fetch data: Status {response.status_code}")
                return None
        except Exception as e:
            st.warning(f"API Error: {str(e)}")
            return None

    def get_game_info(self, game_name: str) -> Dict:
        """Get game information including thumbnail"""
        # Check cache first
        if game_name in st.session_state.bgg_cache:
            return st.session_state.bgg_cache[game_name]

        # Search for game ID
        search_content = self._fetch_api("search", {
            "query": game_name,
            "type": "boardgame",
            "exact": 1
        })
        
        if not search_content:
            return self._create_empty_game_info(game_name)

        try:
            root = ET.fromstring(search_content)
            game = root.find(".//item")
            
            if game is None:
                # Try without exact match
                search_content = self._fetch_api("search", {
                    "query": game_name,
                    "type": "boardgame"
                })
                if search_content:
                    root = ET.fromstring(search_content)
                    game = root.find(".//item")
                
                if game is None:
                    return self._create_empty_game_info(game_name)

            game_id = game.get("id")
            
            # Get game details
            details_content = self._fetch_api("thing", {"id": game_id})
            if not details_content:
                return self._create_empty_game_info(game_name)

            root = ET.fromstring(details_content)
            item = root.find(".//item")
            
            if item is None:
                return self._create_empty_game_info(game_name)

            # Extract game information
            game_info = {
                'name': game_name,
                'id': game_id,
                'thumbnail': None,
                'description': None,
                'categories': [],
                'year': None
            }

            # Get thumbnail
            thumbnail = item.find(".//thumbnail")
            if thumbnail is not None and thumbnail.text:
                game_info['thumbnail'] = thumbnail.text

            # Get description
            description = item.find(".//description")
            if description is not None and description.text:
                game_info['description'] = description.text

            # Get categories
            categories = item.findall(".//link[@type='boardgamecategory']")
            game_info['categories'] = [cat.get("value") for cat in categories]

            # Get year
            year = item.find(".//yearpublished")
            if year is not None:
                game_info['year'] = year.get("value")

            # Cache the result
            st.session_state.bgg_cache[game_name] = game_info
            return game_info

        except Exception as e:
            st.warning(f"Error processing game {game_name}: {str(e)}")
            return self._create_empty_game_info(game_name)

    def _create_empty_game_info(self, game_name: str) -> Dict:
        return {
            'name': game_name,
            'id': None,
            'thumbnail': None,
            'description': None,
            'categories': [],
            'year': None
        }

def display_game_card(game_info: Dict, game_blurb: str):
    """Display a game card with image and details"""
    with st.container(border=True):
        cols = st.columns([1, 2])
        
        with cols[0]:
            if game_info['thumbnail']:
                st.image(game_info['thumbnail'], use_column_width=True)
            else:
                st.image("https://placehold.co/200x200?text=No+Image", use_column_width=True)
        
        with cols[1]:
            st.subheader(game_info['name'])
            st.caption(game_blurb)
            if game_info['year']:
                st.caption(f"Published: {game_info['year']}")
            
            if game_info['categories']:
                st.write("Categories:", ", ".join(game_info['categories']))
            
            if game_info['description']:
                with st.expander("BGG Game Description"):
                    st.write(game_info['description'])
            
            if game_info['id']:
                st.link_button(
                    "View on BGG", 
                    f"https://boardgamegeek.com/boardgame/{game_info['id']}", 
                    use_container_width=True
                )
def display_game_card_no_blurb(game_info: Dict):
    """Display a game card with image and details"""
    with st.container(border=True):
        cols = st.columns([1, 2])
        
        with cols[0]:
            if game_info['thumbnail']:
                st.image(game_info['thumbnail'], use_column_width=True)
            else:
                st.image("https://placehold.co/200x200?text=No+Image", use_column_width=True)
        
        with cols[1]:
            st.subheader(game_info['name'])
            if game_info['year']:
                st.caption(f"Published: {game_info['year']}")
            
            if game_info['categories']:
                st.write("Categories:", ", ".join(game_info['categories']))
            
            if game_info['description']:
                with st.expander("BGG Game Description"):
                    st.write(game_info['description'])
            
            if game_info['id']:
                st.link_button(
                    "View on BGG", 
                    f"https://boardgamegeek.com/boardgame/{game_info['id']}", 
                    use_container_width=True
                )
##########


top2 = st.session_state['Top2']
top2_rename = st.session_state['Top2_rename']

color_persona1 = top2[0]
persona_name1 = top2_rename[0]

color_persona2 = top2[1]
persona_name2 = top2_rename[1]

# def get_categories(url) -> 'List':
#     '''
#     Params: str: Board game url (ex: https://boardgamegeek.com/xmlapi/boardgame/{gameID})

#     Returns: List: List of categories
#     '''
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text)

#     cat_text = soup.find_all('boardgamecategory')
#     cat_list = []
#     for cats in cat_text:
#         s = str(cats)

#         # extract important text between <stuff> important text </stuff>
#         c = re.sub(r'<[^>]+>', '', s)
#         cat_list.append(c)

#     return(cat_list)

# def get_description(url) -> 'str':
#     '''
#     Params: str: Board game url (ex: https://boardgamegeek.com/xmlapi/boardgame/{gameID})

#     Returns: str: string of description
#     '''
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text)

#     cat_text = soup.find_all('description')

#     return(cat_text)

def parse_parenthetical(game_string):

    splitted = game_string.split('(')
    x = splitted[-1].replace(')', '')
    splitted[-1] = x
    return(splitted)

top2 = st.session_state['Top2']
top2_rename = st.session_state['Top2_rename']

color_persona1 = top2[0]
persona_name1 = top2_rename[0]

color_persona2 = top2[1]
persona_name2 = top2_rename[1]

bgg = BGGFetcher()
with st.container(border=True):

    st.title(f'Based off of your specific combination ({top2_rename[0]} and {top2_rename[1]})')

    with open('personality-quiz/personas0.json', 'r') as a:

        data_A = json.load(a)
        most_likely_game = data_A[color_persona1]["Collection"]["Most Likely to Include"]
        games_1 = data_A[color_persona1]["Collection"]["Other Games"][:3]
        games_2 = data_A[color_persona2]["Collection"]["Other Games"][:2]

        st.header(f'A BGG Top 100 Game we think you own: ')
        # st.write(most_likely_game)

        game_info = bgg.get_game_info(most_likely_game)
        display_game_card_no_blurb(game_info)
        # st.markdown("---")

        st.header(f'Other BGG Top 100 games a {top2_rename[0]} + {top2_rename[1]} would enjoy: ')

        # for x in games_1:
        #     st.write(x)
        # for y in games_2:
        #     st.write(y)

        # Combine and display all recommended games
        with st.spinner("Loading game recommendations..."):
            for game_text in games_1 + games_2:
                x = parse_parenthetical(game_text)
                name = x[0]
                flavor = x[-1]

                game_info = bgg.get_game_info(name)
                display_game_card(game_info, flavor)
                # st.markdown("---")

with st.container(border=True):

    st.write('Coming soon: results download button')
    st.page_link("pages/00_start_page.py", label="Retake the Test!", use_container_width=True)