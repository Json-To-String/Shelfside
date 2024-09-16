import streamlit as st
import pandas as pd
import numpy as np


##################
# Question page #
##################

class Handler():

    def __init__(self):
        self.personas = ['Blue', 'Red', 'Clear', 'Black', 'White', 'Green',
                        'Yellow', 'Purple', 'Natural', 'Parchment']

        self.question_options = [
                                'Highly Disagree',
                                'Disagree',
                                'Slightly Disagree',
                                'Neutral',
                                'Slightly Agree',
                                'Agree',
                                'Highly Agree'
                                ]

        self.question_values = [1, 2, 3, 4, 5, 6, 7]
        self.question_mapping = dict(map(lambda i,j : (i,j),
                                self.question_options, self.question_values))

        self.question_dict = {}
        self.question_list = []

        ## playing with the idea of list of dictionaries for weights
        self.question_weights = []

    def get_questions(self):

        with open('questions.txt', 'r') as q:
            for ind, line in enumerate(q):
                if ind % 2 == 0:
                    self.question_list.append(line)
                else:
                    self.question_weights.append(line)

        self.question_dict = dict(map(lambda i,j : (i,j),
                                self.question_list, self.question_weights))


st.title('ShelfSide - What kind of Board Gamer are you?')

page_handler = Handler()
for persona in page_handler.personas:
    if persona not in st.session_state:
        st.session_state[persona] = 0

st.session_state

page_handler.get_questions()

for i in range(5):
    quest = page_handler.question_list[i]
    weight = page_handler.question_weights[i]
    answer = st.radio(f'Question {i}: {quest}', page_handler.question_options)

    ## TODO: parse weights and update session attributes here






st.markdown(
    """<style>
div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 32px;
}
    </style>
    """, unsafe_allow_html=True)

st.session_state

#         ## This seems like not amazing practice but it'll change the radio labelsize
#         st.markdown(
#         """<style>
#         div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
#         font-size: 22px;
# }
#     </style>
#     """, unsafe_allow_html=True)
