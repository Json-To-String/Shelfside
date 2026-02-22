import streamlit as st
import pandas as pd
import numpy as np
import utils.utils as ut

##################
# Question page 3 #
##################

st.title('Let’s throw your friends in the mix and see how you answer!')

progress_text = "Page 3/5"
my_bar = st.progress(0, text=progress_text)
my_bar.progress(40, text=progress_text)

page_num = 3
page_handler = ut.Handler()
page_handler.get_questions('personality-quiz/questions3_mechanical_sociala.txt')

show_errors = st.session_state.get(f'page{page_num}_show_errors', False)
if show_errors:
    st.error("Please answer all questions before continuing.")

with st.form('page_form'):

    page_handler.display_questions(page_num, show_errors=show_errors)

    # Every form must have a submit button.
    submitted = st.form_submit_button('Submit', use_container_width=True, type='primary')
    if submitted:
        if not page_handler.all_answered(page_num):
            st.session_state[f'page{page_num}_show_errors'] = True
            st.rerun()
        else:
            st.session_state[f'page{page_num}_show_errors'] = False
            page_handler.store_answers(page_num)
            st.switch_page('personality-quiz/04_question_page4.py')