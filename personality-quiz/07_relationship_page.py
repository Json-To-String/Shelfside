import streamlit as st
import json
import utils.utils as ut

top2 = st.session_state['Top2']
top2_rename = st.session_state['Top2_rename']

color_persona = top2[0]
name_persona = top2_rename[0]
page_handler = ut.Handler()

with st.container(border=True):
    with open('personality-quiz/personas0.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

        fond_of = data[color_persona]["Fond Of"]
        misunderstand = data[color_persona]["May Have Trouble Understanding"]

        st.title(f'Your Result: The {top2_rename[0]}!')
        persona_image1 = f'res/test_{color_persona.lower()}.png'
        st.image(persona_image1, width=200)

        # Section for "Get Along With" personalities
        st.subheader("Personalities They Get Along With")
        for x in fond_of:
            line = x.split(':')
            color = line[0]
            quote = line[-1]
            name = page_handler.persona_map[color]
            
            with st.expander(f"The {name}"):
                col1, col2 = st.columns([1, 2])
                with col1:
                    im = f'res/test_{color.lower()}.png'
                    st.image(im, width=100)
                with col2:
                    st.write(f"{quote}")

        # Section for "May Have Trouble Understanding" personalities
        st.subheader("Personalities They May Misunderstand")
        for y in misunderstand:
            line = y.split(':')
            color = line[0]
            quote = line[-1]
            name = page_handler.persona_map[color]
            
            with st.expander(f"The {name}"):
                col1, col2 = st.columns([1, 2])
                with col1:
                    im = f'res/test_{color.lower()}.png'
                    st.image(im, width=100)
                with col2:
                    st.write(f"{quote}")


with st.container(border=True):
    st.header("People in the industry you're like")
    

    with st.form('page_form'):

        # Every form must have a submit button.
        submitted = st.form_submit_button(f"3 games for you!",
                                         use_container_width=True, type='primary')
        if submitted:
            st.switch_page('personality-quiz/08_recommend_page.py')