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


# with open('test.json', 'r') as f:
#     data = json.load(f)
#     print(data['Blue']['Strengths'])

df = defaultdict(int)
dictList = [st.session_state[f'page{i+1}_results'] for i in range(4)]

for d in dictList:
    for key, value in d.items():
        df[key] += value
df = dict(df)

persona_map = {
    'Blue' : 'Host',
    'Red' : 'Warhawk',
    'Clear' : 'Collector',
    'Black' : 'Chaos Agent',
    'White' : 'Mediator',
    'Green' : 'Aesthetic',
    'Yellow' : 'Jester',
    'Purple' : 'Befriender',
    'Natural' : 'Purist',
    'Parchment' : 'Storyteller'
}

hex_colors = {
    'Blue': '#1f77b4',
    'Red': '#d62728',
    'Clear': '#7f7f7f',
    'Black': '#2c2c2c',
    'White': '#e6e6e6',
    'Green': '#2ca02c',
    'Yellow': '#ff7f0e',
    'Purple': '#9467bd',
    'Natural': '#8c564b',
    'Parchment': '#bcbd22'
}

df_renamed = {persona_map.get(k, k): v for k, v in df.items()}
df0 = pd.DataFrame(list(df_renamed.items()), columns=['Persona', 'Score'])


### tendencies
# how likely this persona is to host
hosting = {

    'Blue':100,
    'Red':20,
    'Clear':30,
    'Black':10,
    'White':60,
    'Green':70,
    'Yellow':5,
    'Purple':50,
    'Natural':80,
    'Parchment':90

}

# how likely this persona is to research a new game
research_new_game = {

        'Blue':90,
        'Red':50,
        'Clear':80,
        'Black':60,
        'White':50,
        'Green':70,
        'Yellow':40,
        'Purple':40,
        'Natural':100,
        'Parchment':90

}
# how much of a sore loser this persona is
sore_loser = {

        'Blue':10,
        'Red':99,
        'Clear':30,
        'Black':50,
        'White':70,
        'Green':20,
        'Yellow':20,
        'Purple':20,
        'Natural':40,
        'Parchment':30

}

# how likely this persona is to come up with a wacky, unheard of strategy
new_strategy = {

        'Blue':20,
        'Red':60,
        'Clear':60,
        'Black':95,
        'White':60,
        'Green':60,
        'Yellow':70,
        'Purple':60,
        'Natural':50,
        'Parchment':70

}
@st.cache_data
def get_top_two(A):
    return(sorted(A, key=A.get, reverse=True)[:2])

@st.cache_data
def get_top_three(A):
    '''
    Podium???
    '''
    return(sorted(A, key=A.get, reverse=True)[:3])

st.title('Your Results:')
with st.container(border=True):

    # st.button("Calculate my results!")

    progress_text = "Math in progress..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    st.balloons()

    top2 = get_top_two(df)
    top3 = get_top_three(df)

    top3_rename = get_top_three(df_renamed)
    top2_rename = get_top_two(df_renamed)

    # st.metric('Your top two personas: ', top2[0], top2[1])
    # st.bar_chart(df_renamed)

    # Create a bar chart with Altair
    chart = alt.Chart(df0).mark_bar().encode(
        x='Persona',
        y='Score',
        color=alt.Color(
            'Persona',
            scale=alt.Scale(domain=list(persona_map.values()),
            range=list(hex_colors.values())))
    ).properties(
        width=600,  # Customize chart width
        height=400  # Customize chart height
    )

    # Display the chart in Streamlit
    st.altair_chart(chart, use_container_width=True)


    color1 = top2[0]
    color2 = top2[1]

    # st.title(f'You are mostly a: {top3_rename[0]}! with elements of being a {top3_rename[1]} and a {top3_rename[2]}')
    st.title(f'You are mostly a: {top2_rename[0]}! with elements of being a {top2_rename[1]}')
    with open('personality-quiz/personas0.json', 'r') as a, open('personality-quiz/color_combos0.json', 'r') as b:
        data_A = json.load(a)
        data_B = json.load(b)

        for i in range(2):

            color_persona = top2[i]
            name_persona = persona_map[color_persona]

            test_image1 = f'res/test_{color_persona.lower()}.png'
            st.image(test_image1)

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


        st.header(f'Based off of your specific combination ({top2_rename[0]} and {top2_rename[1]})')
        st.write(data_B[color1][color2])

    st.session_state['Top3'] = top3
    st.session_state['Top3_rename'] = top3_rename

    st.session_state['Top2'] = top2
    st.session_state['Top2_rename'] = top2_rename


    with st.container(border=True):
        # col1, col2 = st.columns(2, vertical_alignment = 'center')
        # with col1:
        #     st.page_link("personality-quiz/start_page.py", label="Back to start!", use_container_width=True)
        #
        # with col2:
        st.page_link("personality-quiz/07_relationship_page.py", label=f"See the {top2_rename[0]}'s game night allies and enemies!", use_container_width=True)

    # st.write('TODO: 2) Who you get along with and who you dont get along with ')
    # st.write('TODO: 3) Who are you like from the industry/ShelfSide (plug socials/YT) ')
    # st.write('TODO: 4) Based off of your top two personas, ShelfSide recommends these games + share with your friends')

    # for key in st.session_state:
    #     print(key)
