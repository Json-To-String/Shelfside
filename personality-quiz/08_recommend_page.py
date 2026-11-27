import json
import time
import xml.etree.ElementTree as ET
from typing import Dict, Optional

import streamlit as st

from utils.bggFetcher import request_bgg_xml


class BGGFetcher:
    def __init__(self):
        if 'bgg_cache' not in st.session_state:
            st.session_state.bgg_cache = {}

    @staticmethod
    @st.cache_data(ttl=3600, show_spinner=False)
    def _fetch_api(endpoint: str, params: Dict) -> Optional[bytes]:
        """Generic API fetcher with retry logic"""
        try:
            response = request_bgg_xml(endpoint, params)
            
            # BGG sometimes returns 202 when preparing data
            if response.status_code == 202:
                time.sleep(2)  # Wait and retry
                response = request_bgg_xml(endpoint, params)
            
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
    
    def get_game_info(self, game_name: str, game_id: str) -> Dict:
        """Load the recommendation's game details from its BGG ID."""
        if game_name in st.session_state.bgg_cache:
            return st.session_state.bgg_cache[game_name]

        try:
            details_content = self._fetch_api("thing", {"id": game_id, "stats": 1})
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
        
def display_game_card(game_info: Dict, game_blurb: Optional[str] = None):
    """Display a game card with image and details"""
    with st.container(border=True):
        cols = st.columns([1, 2])
        
        with cols[0]:
            if game_info['thumbnail']:
                st.image(game_info['thumbnail'], width="stretch")
            else:
                st.image("https://placehold.co/200x200?text=No+Image", width="stretch")
        
        with cols[1]:
            st.subheader(game_info['name'])
            if game_blurb is not None:
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
                    width="stretch"
                )


color_persona = st.session_state["Top2"][0]
bgg = BGGFetcher()
with st.container(border=True):
    st.title("3 board games we recommend for you!")

    with open("personality-quiz/personas0.json", encoding="utf-8") as personas_file:
        collection = json.load(personas_file)[color_persona]["Collection"]

    most_likely = collection["Most Likely to Include"]
    game_info = bgg.get_game_info(most_likely["name"], most_likely["bgg_id"])
    display_game_card(game_info)

    with st.spinner("Loading game recommendations..."):
        for game in collection["Other Games"][:2]:
            game_info = bgg.get_game_info(game["name"], game["bgg_id"])
            display_game_card(game_info, game["description"])


with st.form('page_form'):
    col1, col2 = st.columns(2)
    with col1:
        results = st.form_submit_button(f"⏮️ Back to results!",
                                            width="stretch", type='primary')
        if results:
            st.switch_page('personality-quiz/06_results_page.py')
    with col2:
        relationships = st.form_submit_button(f"⏪ Back to relationships!",
                                            width="stretch", type='primary')
        if relationships:
            st.switch_page('personality-quiz/07_relationship_page.py')
    retake = st.form_submit_button(f"Retake the Test! :repeat:",
                                        width="stretch", type='secondary')
    if retake:
        for key in st.session_state.keys():
            del st.session_state[key]
        st.switch_page('personality-quiz/00_start_page.py')