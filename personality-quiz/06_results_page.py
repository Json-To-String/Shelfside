import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px
import json
import utils.utils as ut
from collections import Counter
from collections import defaultdict
import altair as alt

results_page = ut.Handler()

df = defaultdict(int)
dictList = [st.session_state[f'page{i+1}_results'] for i in range(4)]

for d in dictList:
    for key, value in d.items():
        df[key] += value

df = dict(df)

df_renamed = {results_page.persona_map.get(k, k): v for k, v in df.items()}
df0 = pd.DataFrame(list(df_renamed.items()), columns=['Persona', 'Score'])

@st.cache_data
def get_top_two(A):
    return(sorted(A, key=A.get, reverse=True)[:2])

with st.container(border=True):

    top2 = get_top_two(df)
    top2_rename = get_top_two(df_renamed)

    color1 = top2[0]
    color2 = top2[1]

    st.title(f'Your Result: The {top2_rename[0]}!')
    
    with open('personality-quiz/personas0.json', 'r', encoding='utf-8') as a, open('personality-quiz/color_combos0.json', 'r', encoding='utf-8') as b:

        data_A = json.load(a)
        data_B = json.load(b)

        for i in range(1):

            color_persona = top2[i]
            name_persona = results_page.persona_map[color_persona]

            art = f'res/test_{color_persona.lower()}.png'
            st.image(art, width=200)

            blurb = data_A[color_persona]['Blurb']

            st.header(f'The {name_persona}:')
            st.write(f'{blurb}')

            st.subheader('*Strengths:* ')
            for strength in data_A[color_persona]['Strengths']:
                st.write(f'{strength}')

            st.subheader('*Weaknesses:* ')
            for weakness in data_A[color_persona]['Weaknesses']:
                st.write(f'{weakness}')

            st.subheader(f'*Quotes from a {name_persona}*')
            for quote in data_A[color_persona]['Quotes']:
                st.write(f'{quote}')

            st.divider()


        st.header(f'Your answers suggest:')
        st.write(data_B[color1][color2])

    chart = alt.Chart(df0).mark_bar().encode(
        x='Persona',
        y='Score',
        color=alt.Color(
            'Persona',
            scale=alt.Scale(domain=list(results_page.persona_map.values()),
            range=list(results_page.hex_colors.values())))
    ).properties(
        width=600,
        height=400
    )

    st.altair_chart(chart, use_container_width=True)

    st.session_state['Top2'] = top2
    st.session_state['Top2_rename'] = top2_rename

    with st.form('page_form'):

        # Every form must have a submit button.
        submitted = st.form_submit_button(f"Friends and Enemies!",
                                         use_container_width=True, type='primary')
        if submitted:
            st.switch_page('personality-quiz/07_relationship_page.py')