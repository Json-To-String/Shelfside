import streamlit as st
import pandas as pd
import numpy as np
import utils.utils as ut

###################
# Question page 1 #
###################

st.title('ShelfSide - The 10 Board Game Personalities Test')
st.header('Let’s start with some questions about board gaming in general…')

page_handler = ut.Handler()

page_handler.get_questions('personality-quiz/questions1_outside_game_night.txt')
page_handler.display_questions(page_num = 1)

with st.container(border=True):
    st.page_link("personality-quiz/question_page2.py", label="Next Page!")

st.write('for testing: ')
st.session_state
