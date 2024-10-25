import streamlit as st
import requests
import xml.etree.ElementTree as ET
from typing import Optional, Dict
import time

# Use Streamlit's caching for API calls
@st.cache_data(ttl=3600)  # Cache for 1 hour
def fetch_bgg_search(game_name: str) -> requests.Response:
    """Cached BGG search API call"""
    search_url = "https://boardgamegeek.com/xmlapi2/search"
    params = {
        "query": game_name,
        "type": "boardgame"
    }
    return requests.get(search_url, params=params)

@st.cache_data(ttl=3600)  # Cache for 1 hour
def fetch_bgg_details(game_id: str) -> requests.Response:
    """Cached BGG game details API call"""
    details_url = "https://boardgamegeek.com/xmlapi2/thing"
    params = {"id": game_id}
    return requests.get(details_url, params=params)

class BGGStreamlitFetcher:
    def __init__(self):
        # Initialize session state for caching if it doesn't exist
        if 'bgg_cache' not in st.session_state:
            st.session_state.bgg_cache = {}

    def get_game_thumbnail(self, game_name: str, show_progress: bool = True) -> Optional[str]:
        """Get the thumbnail URL for a game with Streamlit progress indicator"""
        # Check session state cache first
        if game_name in st.session_state.bgg_cache:
            return st.session_state.bgg_cache[game_name]

        try:
            if show_progress:
                with st.spinner(f'Fetching image for {game_name}...'):
                    thumbnail_url = self._fetch_thumbnail(game_name)
            else:
                thumbnail_url = self._fetch_thumbnail(game_name)

            # Cache the result in session state
            if thumbnail_url:
                st.session_state.bgg_cache[game_name] = thumbnail_url
            return thumbnail_url

        except Exception as e:
            st.error(f"Error fetching image for {game_name}: {str(e)}")
            return None

    def _fetch_thumbnail(self, game_name: str) -> Optional[str]:
        """Internal method to fetch thumbnail URL"""
        # Search for game
        response = fetch_bgg_search(game_name)
        if response.status_code != 200:
            return None

        root = ET.fromstring(response.content)
        game = root.find(".//item")
        if game is None:
            return None

        game_id = game.get("id")
        
        # Get game details
        response = fetch_bgg_details(game_id)
        if response.status_code != 200:
            return None

        root = ET.fromstring(response.content)
        thumbnail = root.find(".//thumbnail")
        
        return thumbnail.text if thumbnail is not None else None

    @st.cache_data
    def get_multiple_thumbnails(self, game_names: list[str]) -> Dict[str, Optional[str]]:
        """Get thumbnails for multiple games with progress bar"""
        results = {}
        
        # Create a progress bar
        progress_bar = st.progress(0)
        total_games = len(game_names)
        
        for idx, game_name in enumerate(game_names, 1):
            # Update progress bar
            progress_bar.progress(idx / total_games)
            
            results[game_name] = self.get_game_thumbnail(game_name, show_progress=False)
            time.sleep(0.5)  # Be nice to BGG's API
        
        # Clear the progress bar
        progress_bar.empty()
        
        return results

# Example Streamlit app implementation
def main():
    st.title("Board Game Image Fetcher")
    
    fetcher = BGGStreamlitFetcher()
    
    # Single game search
    game_input = st.text_input("Enter a board game name:", "Catan")
    if st.button("Fetch Image"):
        thumbnail_url = fetcher.get_game_thumbnail(game_input)
        if thumbnail_url:
            st.image(thumbnail_url, caption=game_input)
        else:
            st.warning(f"No image found for {game_input}")
    
    # Multiple games example
    st.subheader("Batch Image Fetching")
    games_input = st.text_area("Enter multiple game names (one per line):", "Monopoly\nRisk\nTicket to Ride")
    if st.button("Fetch Multiple Images"):
        games_list = [game.strip() for game in games_input.split("\n") if game.strip()]
        results = fetcher.get_multiple_thumbnails(games_list)
        
        # Display results in columns
        cols = st.columns(min(3, len(games_list)))
        for idx, (game, url) in enumerate(results.items()):
            with cols[idx % 3]:
                if url:
                    st.image(url, caption=game, use_column_width=True)
                else:
                    st.warning(f"No image for {game}")

# For your personality quiz integration
def get_recommended_game_images(recommendations: Dict) -> Dict:
    fetcher = BGGStreamlitFetcher()
    
    with st.spinner("Fetching game images..."):
        for personality, games in recommendations.items():
            for game in games:
                if isinstance(game, dict):
                    game['thumbnail'] = fetcher.get_game_thumbnail(game['name'], show_progress=False)
                else:
                    # If games are stored as strings
                    games[games.index(game)] = {
                        'name': game,
                        'thumbnail': fetcher.get_game_thumbnail(game, show_progress=False)
                    }
    
    return recommendations

if __name__ == "__main__":
    main()