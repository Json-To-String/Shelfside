import streamlit as st
import pandas as pd
import numpy as np

pg = st.navigation([
                    st.Page('page_1.py'),
                    st.Page('page_2.py')])
pg.run()

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

