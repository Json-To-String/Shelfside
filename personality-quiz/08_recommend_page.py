import json
import time
import xml.etree.ElementTree as ET

import requests
import streamlit as st

from utils.bggFetcher import request_bgg_xml


@st.cache_data(ttl=3600, show_spinner=False)
def fetch_game_details(game_id: str) -> dict | None:
    response = request_bgg_xml("thing", {"id": game_id, "stats": 1})
    if response.status_code == 202:
        time.sleep(2)
        response = request_bgg_xml("thing", {"id": game_id, "stats": 1})
    if response.status_code != 200:
        return None

    item = ET.fromstring(response.content).find(".//item")
    if item is None:
        return None

    return {
        "image": item.findtext("image") or item.findtext("thumbnail"),
        "description": item.findtext("description"),
        "categories": [
            category.attrib["value"]
            for category in item.findall('link[@type="boardgamecategory"][@value]')
        ],
        "year": item.find("yearpublished").get("value") if item.find("yearpublished") is not None else None,
    }


def show_game_details(details: dict) -> None:
    if details["image"]:
        st.image(details["image"], width=180)
    if details["year"]:
        st.caption(f"Published in {details['year']}")
    if details["categories"]:
        st.write(", ".join(details["categories"]))
    if details["description"]:
        with st.expander("Game description from BoardGameGeek"):
            st.write(details["description"])


if st.button("Back to results"):
    st.switch_page("personality-quiz/06_results_page.py")

st.title("Three board games for you")
color_persona = st.session_state["Top2"][0]
with open("personality-quiz/personas0.json", encoding="utf-8") as personas_file:
    collection = json.load(personas_file)[color_persona]["Collection"]

games = [collection["Most Likely to Include"], *collection["Other Games"][:2]]
detail_slots = []
for game in games:
    with st.container(border=True):
        st.subheader(game["name"])
        st.write(game["description"].strip())
        st.link_button(
            f'View {game["name"]} on BoardGameGeek',
            f'https://boardgamegeek.com/boardgame/{game["bgg_id"]}',
        )
        detail_slots.append(st.container())

status = st.empty()
with status.container():
    st.html('<p role="status">Loading game details from BoardGameGeek…</p>')

unavailable = False
for game, slot in zip(games, detail_slots, strict=True):
    try:
        details = fetch_game_details(game["bgg_id"])
    except ValueError:
        # A missing token affects every request.
        unavailable = True
        break
    except (requests.RequestException, ET.ParseError):
        details = None

    if details is None:
        unavailable = True
    else:
        with slot:
            show_game_details(details)

message = (
    "Some game details are temporarily unavailable. Use the BoardGameGeek links to learn more."
    if unavailable else "Game details loaded."
)
with status.container():
    st.html(f'<p role="status">{message}</p>')

if st.button("Explore friends & rivals"):
    st.switch_page("personality-quiz/07_relationship_page.py")

if st.button("Retake the quiz"):
    st.session_state.clear()
    st.switch_page("personality-quiz/00_start_page.py")
