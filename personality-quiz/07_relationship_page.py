import streamlit as st
import json


top2 = st.session_state['Top2']
top2_rename = st.session_state['Top2_rename']

# with st.container(border=True):
#     st.graphviz_chart('''
#         digraph {
#             Blue -> Natural
#             Blue -> Purple
#             Red -> Natural
#             Red -> Parchment
#             Clear -> Natural
#             Clear -> Green
#             Black -> Red
#             Black -> Yellow
#             White -> Green
#             White -> Purple
#             Green -> Clear
#             Green -> White
#             Yellow -> Purple
#             Yellow -> Black
#             Purple -> Yellow
#             Purple -> Blue
#             Natural -> Clear
#             Natural -> Green
#             Parchment -> Yellow
#             Parchment -> Green
#         }
#     ''')


# st.title(f'You are mostly a: {top3_rename[0]}! with elements of being a {top3_rename[1]} and a {top3_rename[2]}')
# with open('personality-quiz/personas0.json', 'r') as f:
#     data = json.load(f)
#     for i in range(3):
#
#         color_persona = top3[i]
#         name_persona = persona_map[color_persona]
#         blurb = data[color_persona]['Blurb']
#
#         st.header(f'Persona {i+1}: {name_persona}')
#         st.write(f'{blurb}')
#
#         st.subheader('Strengths: ')
#         for strength in data[color_persona]['Strengths']:
#             st.write(f'{strength}')
#
#         st.subheader('Weaknesses: ')
#         for weakness in data[color_persona]['Weaknesses']:
#             st.write(f'{weakness}')
#
#         st.subheader(f'Quotes from a {name_persona}')
#         for quote in data[color_persona]['Quotes']:
#             st.write(f'{quote}')

with st.container(border=True):
    # col1, col2 = st.columns(2, vertical_alignment = 'center')
    # with col1:
    #     st.page_link("personality-quiz/start_page.py", label="Back to start!", use_container_width=True)
    #
    # with col2:
    st.page_link("personality-quiz/08_recommend_page.py", label="Find out what games you might like!", use_container_width=True)
