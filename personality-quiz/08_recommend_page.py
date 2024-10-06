import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px


top2 = st.session_state['Top2']
top2_rename = st.session_state['Top2_rename']

def get_top_two(A):
    return(sorted(A, key=A.get, reverse=True)[:2])

with st.container(border=True):

    st.metric('Your top two personas: ', top2[0], top2[1])
    st.bar_chart(df)
    st.write('TODO: Based off of those, what games might you like? ')
