import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px


st.session_state
df = st.session_state

# self.personas = ['Blue', 'Red', 'Clear', 'Black', 'White', 'Green', 'Yellow', 'Purple', 'Natural', 'Parchment']


### tendencies
# how likely this persona is to host
hosting = {

    'Blue':100,
    'Red':20,
    'Clear':30,
    'Black':10,
    'White':60,
    'Green':70,
    'Yellow':5,
    'Purple':50,
    'Natural':80,
    'Parchment':90

}

# how likely this persona is to research a new game
research_new_game = {

        'Blue':90,
        'Red':50,
        'Clear':80,
        'Black':60,
        'White':50,
        'Green':70,
        'Yellow':40,
        'Purple':40,
        'Natural':100,
        'Parchment':90

}
# how much of a sore loser this persona is
sore_loser = {

        'Blue':10,
        'Red':99,
        'Clear':30,
        'Black':50,
        'White':70,
        'Green':20,
        'Yellow':20,
        'Purple':20,
        'Natural':40,
        'Parchment':30

}

# how likely this persona is to come up with a wacky, unheard of strategy
new_strategy = {

        'Blue':20,
        'Red':60,
        'Clear':60,
        'Black':95,
        'White':60,
        'Green':60,
        'Yellow':70,
        'Purple':60,
        'Natural':50,
        'Parchment':70

}

def get_top_two(A):
    return(sorted(A, key=A.get, reverse=True)[:2])

with st.container(border=True):

    # st.button("Calculate my results!")

    progress_text = "Math in progress..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    st.balloons()
    top2 = get_top_two(df)

    st.metric('Your top two personas: ', top2[0], top2[1])
    st.bar_chart(df)
    st.write('TODO: 1) Strengths and Weaknesses from your top two AND quotes AND tendencies')

    # st.write('TODO: 2) Who you get along with and who you dont get along with ')
    # st.write('TODO: 3) Based off of your top two, ShelfSide recommends these games ')
    # st.write('TODO: 4) Who are you like from the industry/ShelfSide (plug socials/YT) + share with your friends ')

    # for key in st.session_state:
    #     print(key)