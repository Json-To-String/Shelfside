import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.switch_page_button import switch_page


##############
# Start page #
##############

st.set_page_config(
    page_title="ShelfSide - The 10 Board Game Personalities Test",
    page_icon="🧊",
    # layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# "
    }
)

for i in range(5):
    st.session_state[f'page{i+1}_results'] = 0

# st.session_state
with st.container(border=True):

    col1, col2, col3 = st.columns(3, vertical_alignment = 'center')
    with col1:
        st.image('res/shelfside_logo.png', width=100)
        st.title('ShelfSide')
    st.subtitle('The 10 Board Game Personalities Test')
    with col2:
        st.header('Find out your enemies and allies during game night!')
        st.text('''
            -Which board game designer/influencer are you most like?
            -How much of a sore loser are you?
            -Are you likely to come up with a wacky new strategy?
                ''')
        st.text('< Coming Soon: Art and Game Recommendations >')

        st.page_link("personality-quiz/question_page1.py", label="Start!")
