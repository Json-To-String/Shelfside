import streamlit as st
import requests
import xml.etree.ElementTree as ET
from typing import Optional, Dict
import time

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