import streamlit as st
import pandas as pd
import numpy as np
import time


st.session_state
df = st.session_state

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



    # for key in st.session_state:
    #     print(key)
