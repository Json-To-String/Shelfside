import streamlit as st
import pandas as pd
import numpy as np
import utils.utils as ut

##################
# Question page 5 #
##################

st.title('Almost there! We’ll end with 5 questions solely about hanging out with your friends on game night.')

progress_text = "Page 5/5"
my_bar = st.progress(0, text=progress_text)
my_bar.progress(100, text=progress_text)

page_num = 5
page_handler = ut.Handler()
page_handler.get_questions('pages/questions5_during_games_social.txt')

with st.form('page_form'):

    page_handler.display_questions(page_num)

    # Every form must have a submit button.
    submitted = st.form_submit_button('Calculate My Results!', use_container_width=True, type='primary')
    if submitted:
        page_handler.store_answers(page_num)
        st.switch_page('pages/06_results_page.py')