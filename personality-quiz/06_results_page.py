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

# results_page = ut.Handler()

# df = defaultdict(int)
# dictList = [st.session_state[f'page{i+1}_results'] for i in range(4)]

# for d in dictList:
#     for key, value in d.items():
#         df[key] += value

# df = dict(df)

# df_renamed = {results_page.persona_map.get(k, k): v for k, v in df.items()}
# df0 = pd.DataFrame(list(df_renamed.items()), columns=['Persona', 'Score'])

# @st.cache_data
# def get_top_two(A):
#     return(sorted(A, key=A.get, reverse=True)[:2])

# with st.container(border=True):

#     top2 = get_top_two(df)
#     top2_rename = get_top_two(df_renamed)

#     color1 = top2[0]
#     color2 = top2[1]

#     st.title(f'Your Result: The {top2_rename[0]}!')
    
#     with open('personality-quiz/personas0.json', 'r', encoding='utf-8') as a, open('personality-quiz/color_combos0.json', 'r', encoding='utf-8') as b:

#         data_A = json.load(a)
#         data_B = json.load(b)

#         for i in range(1):

#             color_persona = top2[i]
#             name_persona = results_page.persona_map[color_persona]

#             col1, col2 = st.columns([1, 2])
#             with col1:
#                 art = f'res/test_{color_persona.lower()}.png'
#                 st.image(art, width=200)
#                 blurb = data_A[color_persona]['Blurb']

#             with col2:
#                 st.header(f'The {name_persona}:')
#                 st.write(f'{blurb}')

#                 with st.container(border=True):
#                     st.subheader('*Strengths:* ')
#                     for strength in data_A[color_persona]['Strengths']:
#                         st.write(f'{strength}')

#                 with st.container(border=True):
#                     st.subheader('*Weaknesses:* ')
#                     for weakness in data_A[color_persona]['Weaknesses']:
#                         st.write(f'{weakness}')

#                 with st.container(border=True):
#                     st.subheader(f'*Quotes from a {name_persona}*')
#                     for quote in data_A[color_persona]['Quotes']:
#                         st.write(f'"{quote}"')

#             st.divider()


#         st.header(f'Your answers suggest:')
#         st.write(data_B[color1][color2])

#     chart = alt.Chart(df0).mark_bar().encode(
#         x='Persona',
#         y='Score',
#         color=alt.Color(
#             'Persona',
#             scale=alt.Scale(domain=list(results_page.persona_map.values()),
#             range=list(results_page.hex_colors.values())))
#     ).properties(
#         width=600,
#         height=400
#     )

#     st.altair_chart(chart, use_container_width=True)

#     st.session_state['Top2'] = top2
#     st.session_state['Top2_rename'] = top2_rename


#     with st.form('download_form'):

#         dl_button = st.form_submit_button(f"Save your results! (Coming Soon)",
#                                             use_container_width=True, type='secondary')
#         if dl_button:
#             st.text('...')
        

#     with st.form('page_form'):

#         # Every form must have a submit button.
#         submitted = st.form_submit_button(f"Friends and enemies! ⏩",
#                                          use_container_width=True, type='primary')
#         if submitted:
#             st.switch_page('personality-quiz/07_relationship_page.py')


# Add custom CSS for better styling
st.markdown("""
    <style>
    .results-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: #1f2937;
        text-align: center;
        padding: 2rem 0;
        margin-bottom: 2rem;
        background: linear-gradient(120deg, #f3f4f6 0%, #ffffff 100%);
        border-radius: 10px;
    }
    .persona-header {
        font-size: 1.8rem;
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    .strength-weakness-container {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        border: 1px solid #e9ecef;
    }
    .quote-container {
        font-style: italic;
        padding: 1rem;
        background-color: #f8f9fa;
        border-left: 4px solid #4b5563;
        margin: 0.5rem 0;
    }
    .chart-container {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 2rem 0;
    }
    .button-container {
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

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

# Main results container
with st.container():
    top2 = get_top_two(df)
    top2_rename = get_top_two(df_renamed)
    color1, color2 = top2

    # Title with custom styling
    st.markdown(f"""
        <div class="results-title">
            🎉 Your Result: The {top2_rename[0]}!
        </div>
    """, unsafe_allow_html=True)
    
    with open('personality-quiz/personas0.json', 'r', encoding='utf-8') as a, \
         open('personality-quiz/color_combos0.json', 'r', encoding='utf-8') as b:
        data_A = json.load(a)
        data_B = json.load(b)

        for i in range(1):
            color_persona = top2[i]
            name_persona = results_page.persona_map[color_persona]

            col1, col2 = st.columns([1, 2], gap="large")
            
            with col1:
                art = f'res/test_{color_persona.lower()}.png'
                st.image(art, use_container_width=True)
                with st.container(border=True):
                    st.markdown(f"<p style='font-size: 1.1rem; line-height: 1.6;'>{data_A[color_persona]['Blurb']}</p>",
                              unsafe_allow_html=True)

            with col2:
                st.markdown(f"<h2 class='persona-header'>The {name_persona}</h2>", unsafe_allow_html=True)

                # Strengths section
                with st.container(border=True):
                    st.markdown("### 💪 Strengths")
                    for strength in data_A[color_persona]['Strengths']:
                        st.markdown(f"• {strength}")

                # Weaknesses section
                with st.container(border=True):
                    st.markdown("### 🎯 Weaknesses")
                    for weakness in data_A[color_persona]['Weaknesses']:
                        st.markdown(f"• {weakness}")

                # Quotes section
                with st.container(border=True):
                    st.markdown(f"### 💭 Quotes from a {name_persona}")
                    for quote in data_A[color_persona]['Quotes']:
                        st.markdown(f"""
                            <div class="quote-container">
                                "{quote}"
                            </div>
                        """, unsafe_allow_html=True)

        st.divider()

        # Personality combination insight
        st.markdown(f"### 🔍 Since your second highest was the {top2_rename[-1]},")
        with st.container(border=True):
            st.markdown(f"<p style='font-size: 1.1rem; line-height: 1.6;'>{data_B[color1][color2]}</p>",
                       unsafe_allow_html=True)

        # Chart section
        st.markdown("### 📊 Your Personality Breakdown")
        with st.container(border=True):
            chart = alt.Chart(df0).mark_bar().encode(
                x=alt.X('Persona', sort='-y'),
                y='Score',
                color=alt.Color(
                    'Persona',
                    scale=alt.Scale(
                        domain=list(results_page.persona_map.values()),
                        range=list(results_page.hex_colors.values())
                    )
                )
            ).properties(
                width='container',
                height=400
            ).configure_axis(
                labelFontSize=12,
                titleFontSize=14
            ).configure_title(
                fontSize=16
            )

            st.altair_chart(chart, use_container_width=True)

        st.session_state['Top2'] = top2
        st.session_state['Top2_rename'] = top2_rename

        # Buttons section
        col1, col2 = st.columns(2)
        with col1:
            with st.form('download_form'):
                st.form_submit_button("📥 Save Results (Coming Soon)",
                                    use_container_width=True,
                                    type='secondary')

        with col2:
            with st.form('page_form'):
                submitted = st.form_submit_button("👥 View Friends & Rivals!",
                                               use_container_width=True,
                                               type='primary')
                if submitted:
                    st.switch_page('personality-quiz/07_relationship_page.py')