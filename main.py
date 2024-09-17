import streamlit as st
import pandas as pd
import numpy as np
import os

# here is where the user can switch between pages (only run in home or main.py)
pg = st.navigation([
                   st.Page('personality-quiz/start_page.py'),
                   st.Page('personality-quiz/question_page1.py'),
                   st.Page('personality-quiz/question_page2.py'),
                   st.Page('personality-quiz/question_page3.py'),
                   st.Page('personality-quiz/question_page4.py'),
                   st.Page('personality-quiz/question_page5.py'),
                   st.Page('personality-quiz/results_page.py')
               ])

pg.run()
