import streamlit as st
import pandas as pd
import numpy as np
import utils.utils as ut

##################
# Question page 3 #
##################

st.title('ShelfSide - The 10 Board Game Personalities Test')
st.header('Let’s throw your friends in the mix and see how you answer!')

page_handler = ut.Handler()

page_handler.get_questions('personality-quiz/questions3_mechanical_sociala.txt')
page_handler.display_questions(page_num = 3)

with st.container(border=True):
    st.page_link("personality-quiz/question_page4.py", label="Next Page!")

st.write('for testing: ')
st.session_state
