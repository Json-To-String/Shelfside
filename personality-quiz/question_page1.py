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
        'About': ""
    }
)

st.title('ShelfSide - The 10 Board Game Personalities Test')
st.header('Let’s start with some questions about board gaming in general…')

page_handler = ut.Handler()
#
# # initialized personas in streamlit state
# for persona in page_handler.personas:
#     # if persona not in st.session_state:
#     page_handler.page_results[persona] = 0

page_handler.get_questions('personality-quiz/questions1_outside_game_night.txt')
page_handler.display_questions(page_num = 1)

page_num = 1  # This is for question_page1.py
#
# # Display the questions inside the form
# with st.form(f"form_page_{page_num}"):
#     handler.display_questions(page_num)  # Display the form questions
#
#     # Submit button for the form
#     submitted = st.form_submit_button('Submit')
#     if submitted:
#         handler.store_answers(page_num)  # Store the answers when form is submitted
#
#         # Move to the next page after submission
#         st.session_state.current_page_idx += 1
#         st.experimental_rerun()
# #
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
