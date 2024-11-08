import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.switch_page_button import switch_page

import streamlit.components.v1 as components
import base64

##############
# Start page #
##############

# Initialize session state to store results (for tracking)
for i in range(5):
    st.session_state[f'page{i+1}_results'] = 0

# Update the HTML img src to use base64 encoding
def get_image_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return f"data:image/png;base64,{encoded_string}"

logo_base64 = get_image_base64("css/assets/images/shelfside.png")


# Main content
st.markdown(f"""
<html> 
  <head>
    <title>Hello World</title> 
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="assets/styles.css"> <!-- Ensure the styles.css is in the correct directory -->
  </head>
  <body> 
    <div class="head">
        <div>
            <div class="shelfside">
                <img src="{logo_base64}" alt="Logo" class="logo"> <!-- Using base64 encoded image -->
                <h1>Shelfside</h1>
            </div>
            <h2>The 10 Board Game Personalities Test</h2> 
        </div>
    </div>
    <div class="container">  
        <button class="button-17" role="button" id="start-button">Start Quiz</button>
    </div>
  </body>
</html>
""", unsafe_allow_html=True)

# If the Start Quiz button is clicked, switch to the next page
if st.button('Start Quiz'):
    st.switch_page('pages/01_question_page1.py')
