import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.switch_page_button import switch_page


##############
# Start page #
##############

# st.set_page_config(
#     page_title="ShelfSide - The 10 Board Game Personalities Test",
#     page_icon="res/shelfside_logo.png",
#     # layout="wide",
#     initial_sidebar_state="collapsed",
#     menu_items={
#         'Get Help': 'https://www.extremelycoolapp.com/help',
#         'Report a bug': "https://www.extremelycoolapp.com/bug",
#         'About': "# "
#     }
# )

for i in range(5):
    st.session_state[f'page{i+1}_results'] = 0

# st.session_state
with st.container(border=True):

    col1, col2 = st.columns(2, vertical_alignment = 'center')
    with col1:
        st.image('res/shelfside_logo.png', width=100)
        st.header('The 10 Board Game Personalities Test')
        st.subheader('Find out your enemies and allies during game night!')
    with col2:
        st.title('ShelfSide')
        st.text('''
            -Which board game designer/influencer are you most like?
            -How much of a sore loser are you?
            -Are you likely to come up with a wacky new strategy?
                ''')
        st.text('Note: Your answers may vary based off of which game or game group you’re playing with, try to average out your responses!')
        st.text('< Coming Soon: Art and Game Recommendations >')

        st.page_link("personality-quiz/question_page1.py", label="Start!")
