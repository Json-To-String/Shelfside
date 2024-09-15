import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.switch_page_button import switch_page

question_options = [
        'Highly Disagree', 
        'Disagree', 
        'Slightly Disagree', 
        'Neutral', 
        'Slightly Agree', 
        'Agree', 
        'Highly Agree'
        ]

st.title('ShelfSide - What kind of Board Gamer are you?')
st.image('../res/logo.png')

