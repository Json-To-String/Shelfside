import streamlit as st
import pandas as pd
import numpy as np

## here is where the user can switch between pages (only run in home/main.py)
pg = st.navigation([
                    st.Page('start_page.py'),
                    st.Page('question_page1.py'),
                    st.Page('question_page2.py'),
                    st.Page('question_page3.py'),
                    st.Page('question_page4.py'),
                    st.Page('results_page.py')
                ])

pg.run()
