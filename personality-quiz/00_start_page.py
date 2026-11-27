import streamlit as st

from utils.quiz import SECTION_PAGES, SECTIONS, question_count


st.html(
    '<img class="shelfside-logo" src="./app/static/shelfside_logo.png" '
    'alt="Shelfside" width="144" height="144">'
)
st.title("Find your board-game personality")
st.write("Discover your game-night style, who you click with, and three games to try.")
st.caption(f"{question_count()} questions · {len(SECTIONS)} sections")

if st.button("Start quiz", width="stretch", type="primary"):
    st.switch_page(SECTION_PAGES[0])

st.html(
    '<a href="https://boardgamegeek.com/">'
    '<img src="./app/static/powered_by_bgg.png" alt="Powered by BoardGameGeek" width="160">'
    '</a>'
)
