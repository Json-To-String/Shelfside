import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(
    page_title="ShelfSide - The 10 Board Game Personalities Test",
    page_icon="res/shelfside_logo.png",
    # layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# "
    }
)
# here is where the user can switch between pages (only run in home or main.py)
pg = st.navigation([
                   st.Page('pages/00_start_page.py')
               ])

pg.run()



## Bigger font for questions
st.markdown(
    """<style>
div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 26px;
}
    </style>
    """, unsafe_allow_html=True)

## hide navbar???
st.markdown('''
<style>
.stApp [data-testid="stToolbar"]{
    display:none;
}
</style>
''', unsafe_allow_html=True)

st.set_option("client.showSidebarNavigation", False)
