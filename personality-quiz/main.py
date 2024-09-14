import streamlit as st
import pandas as pd
import numpy as np

st.title('ShelfSide - What kind of Board Gamer are you?')

with open('questions.txt', 'r') as q:

    for line in q:
        print(line)
