import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.switch_page_button import switch_page


##############
# Start page #
##############
with st.container(border=True):

    st.title('ShelfSide - The 10 Board Game Personalities Test')
    st.header('Find out your enemies and allies during game night!')
    st.text('''
        -Which board game designer/influencer are you most like?
        -How much of a sore loser are you?
        -Are you likely to come up with a wacky new strategy?
            ''')
    st.text('< TODO: Art and Recommending Some Games >')
    st.image('res/shelfside_logo.png')
    st.page_link("pages/question_page1.py", label="Start!")
