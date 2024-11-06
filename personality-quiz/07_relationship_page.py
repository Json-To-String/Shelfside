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

        st.title(f'Quotes a {top2_rename[0]} would say to:')
        # st.header(f"We think you'd mostly get along with: ")
        persona_image1 = f'res/test_{color_persona.lower()}.png'
        st.image(persona_image1, width = 300)

        for x in fond_of:

            line = x.split(':')
            color = line[0]
            quote = line[-1]

            name = page_handler.persona_map[color]
            st.subheader(f"The {name}")
            im = f'res/test_{color.lower()}.png'
            st.image(im, width = 200)
            st.write(f"“{quote}“")

        # st.header(f"You may have trouble understanding: ")

        for y in misunderstand:

            line = y.split(':')
            color = line[0]
            quote = line[-1]

            name = page_handler.persona_map[color]
            st.subheader(f"The {name}")
            im = f'res/test_{color.lower()}.png'
            st.image(im, width = 200)
            st.write(f"“{quote}“")


    # with st.container(border=True):

    #     st.page_link("personality-quiz/08_recommend_page.py", label=f"Find out what games a {top2_rename[0]} might like!", use_container_width=True)

    with st.form('page_form'):

        # Every form must have a submit button.
        submitted = st.form_submit_button(f"Find out what games a {top2_rename[0]} might like!",
                                         use_container_width=True, type='primary')
        if submitted:
            st.switch_page('personality-quiz/08_recommend_page.py')