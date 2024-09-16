import streamlit as st
import pandas as pd
import numpy as np



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

#print(question_mapping)

st.title('ShelfSide - What kind of Board Gamer are you?')

#st.radio('Question 1 Text', question_options, horizontal = True)
#st.radio('Question 2 Text', question_options, horizontal = True)
#
#st.selectbox("Pick one", ["cats", "dogs"], horizontal=st.session_state.horizontal)

st.markdown(
    """<style>
div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 32px;
}
    </style>
    """, unsafe_allow_html=True)

st.session_state

# with open('questions.txt', 'r') as q:
#     for line in q:
#         st.radio(f'Question {line}', question_options)
#         answer = st.select_slider(
#                 f'Question {line}',
#                 options = question_options,
#                 )
#
#
#         ## This seems like not amazing practice but it'll change the radio labelsize
#         st.markdown(
#         """<style>
#         div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
#         font-size: 22px;
# }
#     </style>
#     """, unsafe_allow_html=True)
