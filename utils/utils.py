import pandas as pd
import numpy as np
import streamlit as st
from typing import List, Dict, Optional
import requests
from bs4 import BeautifulSoup
import re
from typing import List, Dict, Optional
from functools import lru_cache
import xml.etree.ElementTree as ET


class Handler():

    def __init__(self):
        self.personas = ['Blue', 'Red', 'Clear', 'Black', 'White', 'Green',
                        'Yellow', 'Purple', 'Natural', 'Parchment']

        self.persona_map = {
            'Blue' : 'Host',
            'Red' : 'Warhawk',
            'Clear' : 'Collector',
            'Black' : 'Chaos Agent',
            'White' : 'Mediator',
            'Green' : 'Aesthetic',
            'Yellow' : 'Jester',
            'Purple' : 'Befriender',
            'Natural' : 'Purist',
            'Parchment' : 'Storyteller'
        }

        self.hex_colors = {
            'Blue': '#1f77b4',
            'Red': '#d62728',
            'Clear': '#7f7f7f',
            'Black': '#2c2c2c',
            'White': '#e6e6e6',
            'Green': '#2ca02c',
            # 'Yellow': '#ff7f0e',
            'Yellow': '#ffff00',
            'Purple': '#9467bd',
            'Natural': '#8c564b',
            'Parchment': '#bcbd22'
        }
        
        self.question_options = [
                                'Highly Disagree',
                                'Disagree',
                                'Slightly Disagree',
                                'Neutral',
                                'Slightly Agree',
                                'Agree',
                                'Highly Agree'
                                ]

        # self.question_values = [1, 2, 3, 4, 5, 6, 7]
        self.question_values = [-3, -2, -1, 0, 1, 2, 3]

        # creates dict = {options : values}
        self.question_mapping = dict(map(lambda i,j : (i,j),
                                self.question_options, self.question_values))

        self.question_dict = {}
        self.question_list = []

        ## playing with the idea of list of dictionaries for weights
        self.question_weights = []

        self.question_keys = []

        self.page_results = {persona: None for persona in self.personas}


    def get_questions(self, textfile):
        """
        Called when needing to access questions
        """

        with open(textfile, 'r') as q:

            for ind, line in enumerate(q):

                # Questions are on even indices in the .txt
                if ind % 2 == 0:
                    self.question_list.append(line)

                # weights are on odd indices

                # want to make ex question weight: {Blue : 3, Red: 0, ...}
                else:
                    # start weight dictionary using comprehension
                    weights = {persona: None for persona in self.personas}

                    # strip off parentheses
                    # text = line[1:-1]
                    text = line.replace('(', '').replace(')', '')

                    text = text.split(',')

                    for item in text:
                        item = item.split(' ')

                        # text after split on whitespace looks like:
                        # ['', 'Blue', '-2']
                        # ['', 'Red', '2']

                        color, number = str(item[1]), float(item[-1])
                        weights[color] = number

                    self.question_weights.append(weights)

        # creates dict = {question : weights}
        self.question_dict = dict(map(lambda i,j : (i,j),
                                self.question_list, self.question_weights))

    def display_questions(self, page_num):

    # with st.form('page_form'):
    ## Main Question Loop
        for i in range(len(self.question_list)):
            quest = self.question_list[i]
            # weight = self.question_weights[i]

            quest_key = f'page{page_num}_question{i}'

            # self.question_keys.append(quest_key) ## potentiall superfluous

            answer = st.radio(f'{quest}',
                                self.question_options,
                                horizontal = False,
                                key = quest_key,
                                index = len(self.question_options) // 2)

            st.divider()


    def display_questions_old(self, page_num):

        with st.form('page_form'):
        ## Main Question Loop
            for i in range(len(self.question_list)):
                quest = self.question_list[i]
                # weight = self.question_weights[i]

                quest_key = f'page{page_num}_question{i}'

                # self.question_keys.append(quest_key) ## potentiall superfluous

                answer = st.radio(f'Question {i + 1}: {quest}',
                                    self.question_options,
                                    horizontal = True,
                                    key = quest_key,
                                    # index = len(self.question_options) // 2)
                                    index = None)

                st.divider()

            # Every form must have a submit button.
            submitted = st.form_submit_button('Submit')
            if submitted:
                self.store_answers(page_num)
                st.write('Answers stored, click the button below to move on!')

    def store_answers(self, page_num):

        # self.page_results = {persona: None for persona in self.personas}

        for i in range(len(self.question_list)):
            quest_key = f'page{page_num}_question{i}'
            # quest = self.question_list[i]
            answer = st.session_state.get(quest_key, None)
            weight = self.question_weights[i]

            # st.write(answer)
            if answer is not None:
                for persona in weight:
                    if self.page_results[persona] is None:
                        self.page_results[persona] = 0

                    self.page_results[persona] += weight[persona] * self.question_mapping[answer]

        st.session_state[f'page{page_num}_results'] = self.page_results

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

    def _create_empty_game_info(self, game_name: str) -> Dict:
        return {
            'name': game_name,
            'id': None,
            'thumbnail': None,
            'description': None,
            'categories': [],
            'year': None
        }
    
    def get_game_info(self, game_name: str, game_id: str = None) -> Dict:
        """
        Get game information including thumbnail.
        
        Args:
            game_name (str): Name of the game
            game_id (str, optional): BGG game ID. If provided, bypasses name search.
        
        Returns:
            Dict: Game information including thumbnail, description, etc.
        """
        # Check cache first
        if game_name in st.session_state.bgg_cache:
            return st.session_state.bgg_cache[game_name]

        try:
            # If game_id is provided, skip search and get details directly
            if game_id:
                details_content = self._fetch_api("thing", {
                    "id": game_id,
                    "stats": 1
                })
                
                if not details_content:
                    return self._create_empty_game_info(game_name)
                    
                root = ET.fromstring(details_content)
                item = root.find(".//item")
                
                if item is None:
                    return self._create_empty_game_info(game_name)
            
            # If no game_id provided, search by name
            else:
                search_content = self._fetch_api("search", {
                    "query": game_name,
                    "type": "boardgame"
                })
                
                if not search_content:
                    return self._create_empty_game_info(game_name)

                root = ET.fromstring(search_content)
                games = root.findall(".//item")
                
                if not games:
                    return self._create_empty_game_info(game_name)

                # Take first result
                selected_game = games[0]
                game_id = selected_game.get("id")
                
                # Get details for selected game
                details_content = self._fetch_api("thing", {
                    "id": game_id,
                    "stats": 1
                })
                
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

            # Get thumbnail/image
            image = item.find(".//image")
            if image is not None and image.text:
                game_info['thumbnail'] = image.text
            else:
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
    
    def display_game_card(self, game_info: Dict, game_blurb: str):
        """Display a game card with image and details"""
        with st.container(border=True):
            cols = st.columns([1, 2])
            
            with cols[0]:
                if game_info['thumbnail']:
                    st.image(game_info['thumbnail'], use_container_width=True)
                else:
                    st.image("https://placehold.co/200x200?text=No+Image", use_container_width=True)
            
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
                    
    def display_game_card_no_blurb(self, game_info: Dict):
        """Display a game card with image and details"""
        with st.container(border=True):
            cols = st.columns([1, 2])
            
            with cols[0]:
                if game_info['thumbnail']:
                    st.image(game_info['thumbnail'], use_container_width=True)
                else:
                    st.image("https://placehold.co/200x200?text=No+Image", use_container_width=True)
            
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