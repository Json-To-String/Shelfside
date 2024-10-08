import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px
import json


top2 = st.session_state['Top2']
top2_rename = st.session_state['Top2_rename']

color_persona1 = top2[0]
persona_name1 = top2_rename[0]

color_persona2 = top2[1]
persona_name2 = top2_rename[1]
# def get_top_two(A):
#     return(sorted(A, key=A.get, reverse=True)[:2])

with st.container(border=True):

    # st.metric('Your top two personas: ', top2[0], top2[1])
    st.title(f'Based off of your specific combination ({top2_rename[0]} and {top2_rename[1]})')
    st.title(f'Shelfside thinks: ')

    with open('personality-quiz/personas0.json', 'r') as a:

        data_A = json.load(a)

        st.header(f'Your board game shelf is most likely to include: ')
        st.write(data_A[color_persona1]["Collection"]["Most Likely to Include"])

        st.header(f'Other games a {top2_rename[0]} + {top2_rename[1]} might like: ')
        games_1 = data_A[color_persona1]["Collection"]["Other Games"][:3]
        games_2 = data_A[color_persona2]["Collection"]["Other Games"][:2]
        for x in games_1:
            st.write(x)
        for y in games_2:
            st.write(y)
