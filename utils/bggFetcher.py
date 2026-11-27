import os

import requests
import streamlit as st


def request_bgg_xml(endpoint: str, params: dict) -> requests.Response:
    """Send an authenticated request to the BoardGameGeek XML API."""
    token = os.environ.get("BGG_API_TOKEN", "").strip()
    if not token:
        try:
            token = st.secrets.get("BGG_API_TOKEN", "").strip()
        except FileNotFoundError:
            pass

    if not token:
        raise ValueError("Set BGG_API_TOKEN to load BoardGameGeek data.")

    return requests.get(
        f"https://boardgamegeek.com/xmlapi2/{endpoint}",
        params=params,
        headers={"Authorization": f"Bearer {token}"},
        timeout=10,
    )
