from pathlib import Path

import streamlit as st

from utils.quiz import SECTIONS, START_PAGE

st.set_page_config(
    page_title="ShelfSide - The 10 Board Game Personalities Test",
    page_icon="static/shelfside_logo.png",
    # layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://github.com/Json-To-String/Shelfside/issues',
        'Report a bug': "https://github.com/Json-To-String/Shelfside/issues",
        'About': "# "
    }
)
# here is where the user can switch between pages (only run in home or main.py)
pg = st.navigation([
                   st.Page('personality-quiz/00_start_page.py'),
                   st.Page('personality-quiz/01_question_page1.py'),
                   st.Page('personality-quiz/02_question_page2.py'),
                   st.Page('personality-quiz/03_question_page3.py'),
                   st.Page('personality-quiz/04_question_page4.py'),
                   st.Page('personality-quiz/05_question_page5.py'),
                   st.Page('personality-quiz/06_results_page.py'),
                   st.Page('personality-quiz/07_relationship_page.py'),
                   st.Page('personality-quiz/08_recommend_page.py')
               ], position="hidden")

if pg.url_path in {"results_page", "relationship_page", "recommend_page"}:
    if not all(
        isinstance(st.session_state.get(f"page{section}_results"), dict)
        for section in range(1, len(SECTIONS) + 1)
    ):
        st.switch_page(START_PAGE)
    if pg.url_path != "results_page" and "Top2" not in st.session_state:
        st.switch_page("personality-quiz/06_results_page.py")

st.html(Path(__file__).parent / "CSS" / "Style.css")
pg.run()
