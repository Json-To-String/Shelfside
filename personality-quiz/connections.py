import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px


st.session_state
df = st.session_state

def get_top_two(A):
    return(sorted(A, key=A.get, reverse=True)[:2])

with st.container(border=True):

    st.metric('Your top two personas: ', top2[0], top2[1])
    st.bar_chart(df)
    st.write('TODO: Who you get along with ')
    st.write('TODO: Who you dont get along with ')




    # for key in st.session_state:
    #     print(key)
