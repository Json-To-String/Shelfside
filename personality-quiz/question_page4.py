import streamlit as st
import pandas as pd
import numpy as np
import utils.utils as ut

##################
# Question page 4 #
##################

st.title('ShelfSide - The 10 Board Game Personalities Test')
st.header('Ok! Now let’s make the questions trickier for the home stretch!')

page_handler = ut.Handler()

page_handler.get_questions('personality-quiz/questions4_mechanical_socialb.txt')
page_handler.display_questions(page_num = 4)

with st.container(border=True):
    st.page_link("personality-quiz/question_page5.py", label="Next Page!")

st.write('for testing: ')
st.session_state
