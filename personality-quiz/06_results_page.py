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

@st.cache_data
def get_top_three(A):
    '''
    Podium???
    '''
    return(sorted(A, key=A.get, reverse=True)[:3])

st.title('Your Results:')
with st.container(border=True):

    # st.button("Calculate my results!")

    # progress_text = "Math in progress..."
    # my_bar = st.progress(0, text=progress_text)

    # for percent_complete in range(100):
    #     time.sleep(0.01)
    #     my_bar.progress(percent_complete + 1, text=progress_text)
    # time.sleep(1)
    # my_bar.empty()
    # st.balloons()

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
            scale=alt.Scale(domain=list(results_page.persona_map.values()),
            range=list(results_page.hex_colors.values())))
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

    # st.markdown(f"""
    #     <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 10px; align-items: center;">
    #         <span class="personality-badge chaos-badge">Chaos Agent</span>
    #         <span style="font-size: 1.2em;">with elements of</span>
    #         <span class="personality-badge jester-badge">Jester</span>
    #     </div>
    # """, unsafe_allow_html=True)
    # st.markdown('</div>', unsafe_allow_html=True)        
    # Custom CSS for styling

# st.markdown("""
#     <style>
#     /* Card-like containers */
#     .stCardBox {
#         background-color: white;
#         padding: 20px;
#         border-radius: 10px;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#         margin-bottom: 20px;
#     }
    
#     /* Gradient backgrounds */
#     .main-result {
#         background: linear-gradient(135deg, #f3e8ff 0%, #e0f2fe 100%);
#         padding: 20px;
#         border-radius: 10px;
#         text-align: center;
#         margin-bottom: 20px;
#     }
    
#     /* Badge styling */
#     .personality-badge {
#         display: inline-block;
#         padding: 5px 15px;
#         border-radius: 15px;
#         color: white;
#         font-weight: bold;
#         margin: 5px;
#     }
    
#     .chaos-badge {
#         background-color: #9333ea;
#     }
    
#     .jester-badge {
#         background-color: #f59e0b;
#     }
    
#     /* Quote styling */
#     .quote-box {
#         background-color: #f8f9fa;
#         padding: 10px 15px;
#         border-left: 4px solid;
#         margin: 10px 0;
#         border-radius: 4px;
#     }
    
#     .chaos-quote {
#         border-left-color: #9333ea;
#     }
    
#     .jester-quote {
#         border-left-color: #f59e0b;
#     }
    
#     /* List styling */
#     .custom-list {
#         margin-left: 20px;
#     }
    
#     /* Responsive container */
#     @media (min-width: 768px) {
#         .two-column {
#             display: flex;
#             gap: 20px;
#         }
#     }
#     </style>
#     """, unsafe_allow_html=True)
    
    
    with open('personality-quiz/personas0.json', 'r') as a, open('personality-quiz/color_combos0.json', 'r') as b:
        data_A = json.load(a)
        data_B = json.load(b)

        for i in range(2):

            color_persona = top2[i]
            name_persona = results_page.persona_map[color_persona]

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

            st.divider()


        st.header(f'Based off of your specific combination ({top2_rename[0]} and {top2_rename[1]})')
        st.write(data_B[color1][color2])

    st.session_state['Top3'] = top3
    st.session_state['Top3_rename'] = top3_rename

    st.session_state['Top2'] = top2
    st.session_state['Top2_rename'] = top2_rename


    # with st.container(border=True):

    #     st.page_link("personality-quiz/07_relationship_page.py", label=f"See the {top2_rename[0]}'s game night allies and enemies!", use_container_width=True)

    with st.form('page_form'):

        # Every form must have a submit button.
        submitted = st.form_submit_button(f"See the {top2_rename[0]}'s game night allies and enemies!",
                                         use_container_width=True, type='primary')
        if submitted:
            st.switch_page('personality-quiz/07_relationship_page.py')