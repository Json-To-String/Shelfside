import streamlit as st
import pandas as pd
import numpy as np
import utils.utils as ut

##################
# Question page 4 #
##################

st.title('Ok! Now let’s make the questions trickier for the home stretch!')

progress_text = "Page 4/5"
my_bar = st.progress(0, text=progress_text)
my_bar.progress(60, text=progress_text)

page_num = 4
page_handler = ut.Handler()
page_handler.get_questions('personality-quiz/questions4_mechanical_socialb.txt')

with st.form('page_form'):

    page_handler.display_questions(page_num)

    # Every form must have a submit button.
    submitted = st.form_submit_button('Submit', use_container_width=True, type='primary')
    if submitted:
        page_handler.store_answers(page_num)
        st.switch_page('personality-quiz/05_question_page5.py')

        # with st.container(border=True):
        #     col1, col2 = st.columns(2, vertical_alignment = 'center')
        #     with col1:
        #         st.page_link("personality-quiz/03_question_page3.py", label="Prev Page!", use_container_width=True)
        #
        #     with col2:
        #         st.page_link("personality-quiz/05_question_page5.py", label="Next Page!", use_container_width=True)
