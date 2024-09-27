import streamlit as st
import pandas as pd
import numpy as np
import utils.utils as ut

##################
# Question page 5 #
##################

# st.title('ShelfSide - The 10 Board Game Personalities Test')
# st.header('Almost there! We’ll end with 5 questions solely about hanging out with your buddies on game night.')
st.title('Almost there! We’ll end with 5 questions solely about hanging out with your buddies on game night.')

progress_text = "Page 5/5"
my_bar = st.progress(0, text=progress_text)
my_bar.progress(100, text=progress_text)

page_num = 5
page_handler = ut.Handler()
page_handler.get_questions('personality-quiz/questions5_during_games_social.txt')

with st.form('page_form'):

    page_handler.display_questions(page_num)

    # Every form must have a submit button.
    submitted = st.form_submit_button('Submit', use_container_width=True)
    if submitted:
        page_handler.store_answers(page_num)
        st.write('Answers stored, click the button below to move on!')

        with st.container(border=True):
            col1, col2 = st.columns(2, vertical_alignment = 'center')
            with col1:
                st.page_link("personality-quiz/question_page4.py", label="Prev Page!", use_container_width=True)

            with col2:
                st.page_link("personality-quiz/results_page.py", label="Calculate My Results!", use_container_width=True)

#
# st.write('for testing: ')
# st.session_state
