import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px
import json
import utils.utils as ut

top2 = st.session_state['Top2']
top2_rename = st.session_state['Top2_rename']

color_persona1, color_persona2 = top2[0], top2[1]
persona_name1, persona_name2 = top2_rename[0], top2_rename[1]

bgg = ut.BGGFetcher()
with st.container(border=True):

    st.title(f'3 board games we recommend for you!')
    with open('personality-quiz/personas0.json', 'r', encoding='utf-8') as a:

        data_A = json.load(a)
        other_games = data_A[color_persona1]["Collection"]["Other Games"][:2]

        most_likely = data_A[color_persona1]["Collection"]["Most Likely to Include"]
        game_info = bgg.get_game_info(most_likely["name"], most_likely["bgg_id"])

        bgg.display_game_card_no_blurb(game_info)

        for game in other_games:
            game_info = bgg.get_game_info(game["name"], game["bgg_id"])
            bgg.display_game_card(game_info, game["description"])

with st.form('page_form'):
    col1, col2 = st.columns(2)
    with col1:
        results = st.form_submit_button(f"⏮️ Back to results!",
                                            use_container_width=True, type='primary')
        if results:
            st.switch_page('personality-quiz/06_results_page.py')
    with col2:
        relationships = st.form_submit_button(f"⏪ Back to relationships!",
                                            use_container_width=True, type='primary')
        if relationships:
            st.switch_page('personality-quiz/07_relationship_page.py')
    retake = st.form_submit_button(f"Retake the Test! :repeat:",
                                        use_container_width=True, type='secondary')
    if retake:
        for key in st.session_state.keys():
            del st.session_state[key]
        st.switch_page('personality-quiz/00_start_page.py')