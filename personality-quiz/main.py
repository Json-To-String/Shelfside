import streamlit as st
import pandas as pd
import numpy as np

## here is where the user can switch between pages (only run in home/main.py)
pg = st.navigation([
                    st.Page('personality_quiz/start_page.py'),
                    st.Page('personality_quiz/question_page1.py'),
                    st.Page('personality_quiz/question_page2.py'),
                    st.Page('personality_quiz/question_page3.py'),
                    st.Page('personality_quiz/question_page4.py'),
                    st.Page('personality_quiz/results_page.py')
                ])

pg.run()
