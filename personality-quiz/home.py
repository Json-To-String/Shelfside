import streamlit as st
import pandas as pd
import numpy as np

## here is where the user can switch between pages (only run in home/main.py)
pg = st.navigation([
                    st.Page('page_1.py'),
                    st.Page('page_2.py')])
pg.run()


# class Handler():
#
#     def __init__(self):
#         self.personas = ['Blue', 'Red', 'Clear', 'Black', 'White', 'Green',
#                         'Yellow', 'Purple', 'Natural', 'Parchment']
#
#         self.question_options = [
#                                 'Highly Disagree',
#                                 'Disagree',
#                                 'Slightly Disagree',
#                                 'Neutral',
#                                 'Slightly Agree',
#                                 'Agree',
#                                 'Highly Agree'
#                                 ]
#
#         self.question_values = [1, 2, 3, 4, 5, 6, 7]
#         self.question_mapping = dict(map(lambda i,j : (i,j),
#                                 self.question_options, self.question_values))
#
#         self.question_dict = {}
#         self.question_list = []
#         self.question_weights = []
#
#     def get_questions(self):
#
#         with open('questions.txt', 'r') as q:
#             for ind, line in enumerate(q):
#                 if ind % 2 == 0:
#                     self.question_list.append(line)
#                 else:
#                     self.question_weights.append(line)

# homepage_handler = Handler()
# for persona in homepage_handler.personas:
#     if persona not in st.session_state:
#         st.session_state[persona] = 0
#
# st.session_state
#
# homepage_handler.get_questions()
#
# for i in range(5):
#     print(homepage_handler.question_list[i])
