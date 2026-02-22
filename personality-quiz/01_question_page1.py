import streamlit as st
import pandas as pd
import numpy as np
import utils.utils as ut

###################
# Question page 1 #
###################

st.title('Let’s start with some questions about board gaming in general…')

progress_text = "Page 1/5"
my_bar = st.progress(0, text=progress_text)

page_num = 1
page_handler = ut.Handler()
page_handler.get_questions('personality-quiz/questions1_outside_game_night.txt')

with st.form('page_form'):

    page_handler.display_questions(page_num)

    # Every form must have a submit button.
    submitted = st.form_submit_button('Submit', use_container_width=True, type='primary')
    if submitted:
        if not page_handler.all_answered(page_num):
            st.error("Please answer all questions before continuing.")
        else:
            page_handler.store_answers(page_num)
            st.switch_page('personality-quiz/02_question_page2.py')