import streamlit as st
import pandas as pd
import numpy as np
import utils.utils as ut

##################
# Question page 5 #
##################

st.title('ShelfSide - The 10 Board Game Personalities Test')
st.header('Almost there! We’ll end with 5 questions solely about hanging out with your buddies on game night.')

page_handler = ut.Handler()

page_handler.get_questions('personality-quiz/questions5_during_games_social.txt')
page_handler.display_questions(page_num = 5)

with st.container(border=True):
    st.page_link("personality-quiz/results_page.py", label="Calculate My Results!")

st.write('for testing: ')
st.session_state
