import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.switch_page_button import switch_page

import streamlit.components.v1 as components

##############
# Start page #
##############

for i in range(5):
    st.session_state[f'page{i+1}_results'] = 0


# set_background('res/start_bg.png')

# # st.session_state
# with st.container(border=True):

st.image('res/shelfside_logo.png', width=100)
#     st.title('ShelfSide')
#     st.header('The 10 Board Game Personalities Test')
#     st.subheader('- Find out your enemies and allies during game night!')
#     # st.subheader('''
#     #     -Which board game designer/influencer are you most like?
#     #     -How much of a sore loser are you?
#     #     -Are you likely to come up with a wacky new strategy?
#     #         ''')
#     st.subheader('- Which board game designer/influencer are you most like?')
#     st.subheader('- How much of a sore loser are you?')
#     st.subheader('- Are you likely to come up with a wacky new strategy?')
#     st.subheader('Note: Your answers may vary based off of which game or game group you’re playing with, try to average out your responses!')
#     st.subheader('< Coming Soon: Art and Game Recommendations >')

# Custom styling
st.markdown("""
    <style>
    /* Global styles */
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* Title styling */
    .main-title {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .main-title img {
        margin-bottom: 1rem;
    }
    
    .main-title h1 {
        color: #1E1E1E;
        margin-bottom: 0.5rem;
    }
    
    /* Subheader styling */
    .feature-list {
        margin: 2rem 0;
        text-align: left;
    }
    
    .feature-list h3 {
        color: #424242;
        margin-bottom: 0.5rem;
        font-size: 1.2rem;
    }
    
    /* Note styling */
    .note-text {
        font-style: italic;
        color: #666;
        margin: 2rem 0;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 8px;
    }
    
    /* Coming soon styling */
    .coming-soon {
        text-align: center;
        color: #666;
        margin-top: 2rem;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #FF4B4B !important;
        color: white !important;
        padding: 0.75rem 2rem !important;
        font-size: 1.1rem !important;
        border-radius: 8px !important;
        width: 100% !important;
        margin-top: 2rem !important;
    }
    
    .stButton > button:hover {
        background-color: #FF3131 !important;
    }
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .main-title img {
            width: 80px !important;
        }
        
        .main-title h1 {
            font-size: 1.8rem;
        }
        
        .feature-list h3 {
            font-size: 1.1rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Update the HTML img src to use base64 encoding
import base64

def get_image_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return f"data:image/png;base64,{encoded_string}"

logo_base64 = get_image_base64("res/shelfside_logo.png")

# Main content
st.markdown("""
    <div class="main-title">
        <h1>ShelfSide</h1>
        <h2>The 10 Board Game Personalities Test</h2>
    </div>
    
    <div class="feature-list">
        <h3>- Find out your enemies and allies during game night!</h3>
        <h3>- Which board game designer/influencer are you most like?</h3>
        <h3>- How much of a sore loser are you?</h3>
        <h3>- Are you likely to come up with a wacky new strategy?</h3>
    </div>
    
    <div class="note-text">
        Note: Your answers may vary based off of which game or game group you're playing with, try to average out your responses!
    </div>
    
    <div class="coming-soon">
        &lt; Coming Soon: Art and Game Recommendations &gt;
    </div>
""", unsafe_allow_html=True)


# Start button form
with st.form('page_form'):
    submitted = st.form_submit_button('Start your test!', use_container_width=True, type='primary')
    if submitted:
        st.switch_page('01_question_page1')