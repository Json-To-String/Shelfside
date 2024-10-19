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

# st.session_state
with st.container(border=True):

    st.image('res/shelfside_logo.png', width=100)
    st.title('ShelfSide')
    st.header('The 10 Board Game Personalities Test')
    st.subheader('Find out your enemies and allies during game night!')
    st.subheader('''
        -Which board game designer/influencer are you most like?
        -How much of a sore loser are you?
        -Are you likely to come up with a wacky new strategy?
            ''')
    st.subheader('Note: Your answers may vary based off of which game or game group you’re playing with, try to average out your responses!')
    st.subheader('< Coming Soon: Art and Game Recommendations >')
with st.form('page_form'):

    # page_handler.display_questions(page_num)

    # Every form must have a submit button.
    submitted = st.form_submit_button('Start!', use_container_width=True, type='primary')
    if submitted:
        # page_handler.store_answers(page_num)
        st.switch_page('personality-quiz/01_question_page1.py')
    # st.page_link("personality-quiz/01_question_page1.py", label="Start!")

# components.html(
#     """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>ShelfSide Board Game Quiz</title>
#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             margin: 0;
#             padding: 0;
#             background-color: #f5f5f5;
#             text-align: center;
#         }
#
#         .header {
#             background-color: #1a1a1a;
#             color: white;
#             padding: 40px;
#         }
#
#         .header-content {
#             display: flex;
#             align-items: center;
#             justify-content: center;
#         }
#
#         .logo {
#             width: 60px;
#             height: 60px;
#             margin-right: 20px;
#         }
#
#         .header h1 {
#             font-size: 48px;
#             margin: 0;
#         }
#
#         .header p {
#             font-size: 24px;
#             margin: 10px 0;
#         }
#
#         .start-btn {
#             background-color: #ff4a4a;
#             color: white;
#             padding: 15px 30px;
#             font-size: 24px;
#             border: none;
#             border-radius: 30px;
#             cursor: pointer;
#             margin-top: 30px;
#         }
#
#         .start-btn:hover {
#             background-color: #e03a3a;
#         }
#
#         .table-img {
#             margin-top: 50px;
#             position: relative;
#             width: 50%;
#             margin-left: auto;
#             margin-right: auto;
#         }
#
#         .table-img img {
#             width: 100%;
#             height: auto;
#             border-radius: 20px;
#         }
#
#         .faces {
#             display: flex;
#             justify-content: space-around;
#             margin-top: 20px;
#             max-width: 80%;
#             margin-left: auto;
#             margin-right: auto;
#         }
#
#         .face {
#             border-radius: 50%;
#             overflow: hidden;
#             width: 100px;
#             height: 100px;
#         }
#
#         .face img {
#             width: 100%;
#             height: 100%;
#             object-fit: cover;
#         }
#
#         .social-icons {
#             margin-top: 30px;
#         }
#
#         .social-icons img {
#             width: 30px;
#             margin: 0 10px;
#             cursor: pointer;
#         }
#     </style>
# </head>
# <body>
#
#     <div class="header">
#         <div class="header-content">
#             <img class="logo" src="res/shelfside_logo.png" alt="Logo">
#             <h1>ShelfSide</h1>
#         </div>
#         <p>The 10 Board Game Personalities Test</p>
#     </div>
#
#     <button class="start-btn">Start quiz</button>
#
#     <div class="table-img">
#         <img src="/mnt/data/start_bg.png" alt="Board Game">
#     </div>
#
#     <div class="faces">
#         <div class="face"><img src="https://i.imgur.com/xyz1.png" alt="Face 1"></div>
#         <div class="face"><img src="https://i.imgur.com/xyz2.png" alt="Face 2"></div>
#         <div class="face"><img src="https://i.imgur.com/xyz3.png" alt="Face 3"></div>
#         <div class="face"><img src="https://i.imgur.com/xyz4.png" alt="Face 4"></div>
#     </div>
#
#     <div class="social-icons">
#         <img src="https://i.imgur.com/instagram-icon.png" alt="Instagram">
#         <img src="https://i.imgur.com/youtube-icon.png" alt="YouTube">
#     </div>
#
# </body>
# </html>
#
#
#     """,
#     height=600,
# )
