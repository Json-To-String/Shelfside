import streamlit as st
import pandas as pd
import numpy as np
import utils.utils as ut

##################
# Question page 2 #
##################

st.title('Now it’s time for game night! What is your mental approach?')

progress_text = "Page 2/5"
my_bar = st.progress(0, text=progress_text)
my_bar.progress(20, text=progress_text)

page_num = 2
page_handler = ut.Handler()
page_handler.get_questions('personality-quiz/questions2_during_games_mechanical.txt')

with st.form('page_form'):

    page_handler.display_questions(page_num)

    # Every form must have a submit button.
    submitted = st.form_submit_button('Submit', use_container_width=True, type='primary')
    if submitted:
        page_handler.store_answers(page_num)
        st.switch_page('personality-quiz/03_question_page3.py')