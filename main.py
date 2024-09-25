import streamlit as st
import pandas as pd
import numpy as np
import os

# here is where the user can switch between pages (only run in home or main.py)
pg = st.navigation([
                   st.Page('personality-quiz/start_page.py'),
                   st.Page('personality-quiz/question_page1.py'),
                   st.Page('personality-quiz/question_page2.py'),
                   st.Page('personality-quiz/question_page3.py'),
                   st.Page('personality-quiz/question_page4.py'),
                   st.Page('personality-quiz/question_page5.py'),
                   st.Page('personality-quiz/results_page.py')
               ])

pg.run()

# # Initialize current page index in session state
# if 'current_page_idx' not in st.session_state:
#     st.session_state.current_page_idx = 0  # Start at the first page
#
# # Define the list of pages
# pages = [
#     'pages/start_page.py',
#     'pages/question_page1.py',
#     'pages/question_page2.py',
#     'pages/question_page3.py',
#     'pages/question_page4.py',
#     'pages/question_page5.py',
#     'pages/results_page.py'
# ]
#
# # Function to go to the next page
# def go_to_next_page():
#     if st.session_state.current_page_idx < len(pages) - 1:
#         st.session_state.current_page_idx += 1
#     st.experimental_rerun()
#
# # Dynamically run the current page
# current_page = pages[st.session_state.current_page_idx]
# exec(open(current_page).read())
