import streamlit as st
import pandas as pd
import numpy as np
import utils.utils as ut
###################
# Question page 1 #
###################

st.set_page_config(
    page_title="ShelfSide - The 10 Board Game Personalities Test",
    page_icon="🧊",
    # layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title('ShelfSide - The 10 Board Game Personalities Test')
st.header('Let’s start with some questions about board gaming in general…')

page_handler = ut.Handler()

# initialized personas in streamlit state
for persona in page_handler.personas:
    # if persona not in st.session_state:
    st.session_state[persona] = 0

# st.session_state

page_handler.get_questions('personality-quiz/questions1_outside_game_night.txt')

page_handler.update_questions()

## Hacky css solution to get question labels bigger
st.markdown(
    """<style>
div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 32px;
}
    </style>
    """, unsafe_allow_html=True)

with st.container(border=True):
    st.page_link("personality-quiz/question_page2.py", label="Next Page!")

st.write('for testing: ')
st.session_state
