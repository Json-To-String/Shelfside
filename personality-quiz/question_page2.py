import streamlit as st
import pandas as pd
import numpy as np

##################
# Question page 2 #
##################

# class Question():
# """
# Plan for Question object to have text and weights for each
# """
#     def __init__(self):
#         self.text = ''
#         self.weights = {}

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

        # self.question_values = [1, 2, 3, 4, 5, 6, 7]
        self.question_values = [-3, -2, -1, 0, 1, 2, 3]

        # creates dict = {options : values}
        self.question_mapping = dict(map(lambda i,j : (i,j),
                                self.question_options, self.question_values))

        self.question_dict = {}
        self.question_list = []

        ## playing with the idea of list of dictionaries for weights
        self.question_weights = []

    def get_questions(self, textfile):
        """
        Called when needing to access questions
        """

        with open(textfile, 'r') as q:

            for ind, line in enumerate(q):

                # Questions are on even indices in the .txt
                if ind % 2 == 0:
                    self.question_list.append(line)

                # weights are on odd indices

                # want to make ex question weight: {Blue : 3, Red: 0, ...}
                else:
                    # start weight dictionary using comprehension
                    weights = {persona: None for persona in self.personas}

                    # strip off parentheses
                    # text = line[1:-1]
                    text = line.replace('(', '').replace(')', '')

                    text = text.split(',')

                    for item in text:
                        item = item.split(' ')

                        # text after split on whitespace looks like:
                        # ['', 'Blue', '-2']
                        # ['', 'Red', '2']

                        color, number = str(item[1]), float(item[-1])
                        weights[color] = number

                    self.question_weights.append(weights)

        # creates dict = {question : weights}
        self.question_dict = dict(map(lambda i,j : (i,j),
                                self.question_list, self.question_weights))


st.title('ShelfSide - The 10 Board Game Personalities Test')
st.header('Now it’s time for game night! What is your mental approach?')

page_handler = Handler()

# # initialized personas in streamlit state
# for persona in page_handler.personas:
#     # if persona not in st.session_state:
#     st.session_state[persona] = 0

# st.session_state

page_handler.get_questions('questions2_during_games_mechanical.txt')

## Main Question Loop
for i in range(len(page_handler.question_list)):
    quest = page_handler.question_list[i]
    weight = page_handler.question_weights[i]
    answer = st.radio(f'Question {i + 1}: {quest}',
                        page_handler.question_options,
                        horizontal = True,
                        index = len(page_handler.question_options)//2)

    for key in weight:

        ## use weights to update session attributes here
        st.session_state[key] += weight[key] * page_handler.question_mapping[answer]

    st.divider()

## Hacky css solution to get question labels bigger
st.markdown(
    """<style>
div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 32px;
}
    </style>
    """, unsafe_allow_html=True)


## On click, move to next page:
# st.button('Calculate my results', on_click=st.switch_page("results_page.py"))
st.page_link("question_page3.py", label="Next Page!")

st.write('for testing: ')
st.session_state
