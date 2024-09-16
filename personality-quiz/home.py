import streamlit as st
import pandas as pd
import numpy as np

pg = st.navigation([
                    st.Page('page_1.py'),
                    st.Page('page_2.py')])
pg.run()


# class Handler():
#
#     def __init__(self):
#         self.personas
personas = ['Blue', 'Red', 'Clear',
            'Black', 'White', 'Green',
            'Yellow', 'Purple', 'Natural', 'Parchment']
question_options = [
        'Highly Disagree',
        'Disagree',
        'Slightly Disagree',
        'Neutral',
        'Slightly Agree',
        'Agree',
        'Highly Agree'
        ]

question_values = [1, 2, 3, 4, 5, 6, 7]

question_mapping = dict(map(lambda i,j : (i,j) , question_options, question_values))

question_dict = {}
question_list = []
question_weights = []
with open('questions.txt', 'r') as q:
    for ind, line in enumerate(q):
        if ind % 2 == 0:
            question_list.append(line)
        else:
            question_weights.append(line)


for persona in personas:
    if persona not in st.session_state:
        st.session_state[persona] = 0

st.session_state
for i in range(5):
    print(question_list[i])
