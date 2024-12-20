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

# Custom CSS
st.markdown("""
    <style>
        /* Modern font stack */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
        
        .main-title {
            text-align: center;
            padding: 2rem;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            border-radius: 20px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .main-title img {
            margin-bottom: 1rem;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease;
        }
        
        .main-title img:hover {
            transform: scale(1.05);
        }
        
        .main-title h1 {
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            font-size: 2.5rem;
            color: #2c3e50;
            margin: 1rem 0;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }
        
        .main-title h2 {
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
            color: #34495e;
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }
        
        .feature-list {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            margin: 2rem 0;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }
        
        .feature-list h3 {
            font-family: 'Poppins', sans-serif;
            color: #34495e;
            margin: 1rem 0;
            font-size: 1.2rem;
            display: flex;
            align-items: center;
        }
        
        .feature-list h3:before {
            content: "🎲";
            margin-right: 10px;
            font-size: 1.2rem;
        }
        
        .note-text {
            font-family: 'Poppins', sans-serif;
            background: #fff8e1;
            padding: 1rem;
            border-left: 4px solid #ffd54f;
            border-radius: 0 10px 10px 0;
            margin: 2rem 0;
            color: #5d4037;
        }
        
        .coming-soon {
            font-family: 'Poppins', sans-serif;
            text-align: center;
            color: #7f8c8d;
            padding: 1rem;
            background: #f7f9fc;
            border-radius: 10px;
            font-style: italic;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.7; }
            100% { opacity: 1; }
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .main-title h1 {
                font-size: 2rem;
            }
            
            .main-title h2 {
                font-size: 1.2rem;
            }
            
            .feature-list h3 {
                font-size: 1rem;
            }
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
@media (max-width: 768px) {
    /* Ensure full width and padding on mobile */
    .stApp {
        max-width: 100% !important;
        padding: 0 10px !important;
    }

    /* Adjust main title */
    .main-title {
        padding: 1rem !important;
        border-radius: 10px !important;
    }

    .main-title img {
        width: 120px !important;
        height: auto !important;
        margin-bottom: 0.5rem !important;
    }

    .main-title h1 {
        font-size: 1.5rem !important;
        margin: 0.5rem 0 !important;
    }

    .main-title h2 {
        font-size: 1rem !important;
        margin-bottom: 0.5rem !important;
    }

    /* Feature list adjustments */
    .feature-list {
        padding: 1rem !important;
        margin: 1rem 0 !important;
    }

    .feature-list h3 {
        font-size: 0.9rem !important;
        margin: 0.5rem 0 !important;
    }

    .feature-list h3:before {
        font-size: 1rem !important;
        margin-right: 5px !important;
    }

    /* Button styling */
    .stButton > button {
        padding: 0.5rem 1rem !important;
        font-size: 1rem !important;
        margin-top: 1rem !important;
    }

    /* Note and coming soon sections */
    .note-text,
    .coming-soon {
        padding: 0.75rem !important;
        margin: 1rem 0 !important;
        font-size: 0.9rem !important;
    }

    /* Ensure content doesn't overflow */
    * {
        max-width: 100% !important;
        box-sizing: border-box !important;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="main-title">
        <img src="./app/static/shelfside_logo.png" alt="Shelfside" width="200" height="200">
        <h1>Shelfside</h1>
        <h2>The 10 Board Game Personalities Test</h2>
    </div>
    
    <div class="feature-list">
        <h3>Find out your enemies and allies during game night!</h3>
        <h3>How much of a sore loser are you?</h3>
        <h3>Are you likely to come up with a wacky new strategy?</h3>
    </div>

""", unsafe_allow_html=True)

with st.form('page_form'):
    submitted = st.form_submit_button('Start your test!', use_container_width=True, type='primary')
    if submitted:
        st.switch_page('personality-quiz/01_question_page1.py')