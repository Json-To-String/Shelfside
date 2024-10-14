import streamlit as st
import json
import utils.utils as ut

top2 = st.session_state['Top2']
top2_rename = st.session_state['Top2_rename']

color_persona = top2[0]
name_persona = top2_rename[0]
page_handler = ut.Handler()

with st.container(border=True):

    with open('personality-quiz/personas0.json', 'r') as f:
        data = json.load(f)

        fond_of = data[color_persona]["Fond Of"]
        misunderstand = data[color_persona]["May Have Trouble Understanding"]

        st.title(f'Since you answered mostly as a {top2_rename[0]}')
        st.header(f"We think you'd mostly get along with: ")

        for x in fond_of:

            line = x.split(':')
            color = line[0]
            quote = line[-1]

            name = page_handler.persona_map[color]
            st.subheader(f"The {name}")
            st.write(f"“{quote}“")

        st.header(f"You may have trouble understanding: ")

        for y in misunderstand:

            line = y.split(':')
            color = line[0]
            quote = line[-1]

            name = page_handler.persona_map[color]
            st.subheader(f"The {name}")
            st.write(f"“{quote}“")
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
        st.page_link("personality-quiz/08_recommend_page.py", label=f"Find out what games a {top2_rename[0]} might like!", use_container_width=True)
