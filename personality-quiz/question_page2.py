import streamlit as st
import pandas as pd
import numpy as np
import utils.utils as ut

##################
# Question page 2 #
##################

st.title('ShelfSide - The 10 Board Game Personalities Test')
st.header('Now it’s time for game night! What is your mental approach?')

page_handler = ut.Handler()

page_handler.get_questions('personality-quiz/questions2_during_games_mechanical.txt')
page_handler.display_questions(page_num = 2)

## Hacky css solution to get question labels bigger
st.markdown(
    """<style>
div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 32px;
}
    </style>
    """, unsafe_allow_html=True)

with st.container(border=True):
    st.page_link("personality-quiz/question_page3.py", label="Next Page!")

st.write('for testing: ')
st.session_state
