import streamlit as st
import json
from pathlib import Path
import utils.utils as ut

top2 = st.session_state['Top2']
top2_rename = st.session_state['Top2_rename']

color_persona = top2[0]
name_persona = top2_rename[0]
page_handler = ut.Handler()

if st.button("Back to results"):
    st.switch_page("personality-quiz/06_results_page.py")

st.title("Friends & rivals")
if st.button("See my game recommendations", width="stretch", type="primary"):
    st.switch_page("personality-quiz/08_recommend_page.py")

with st.container(border=True):
    with open('personality-quiz/personas0.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

        fond_of = data[color_persona]["Fond Of"]
        misunderstand = data[color_persona]["May Have Trouble Understanding"]

        #st.title(f'Your Result: The {top2_rename[0]}!')
        favor_image = f'res/relationships/{name_persona.lower()}_favors.png'
        st.image(favor_image)

        col1, col2 = st.columns(2)
        with col1:
            col1.subheader("How you might talk to the personalities you get along with:")
            for x in fond_of:
                line = x.split(':')
                color = line[0]
                quote = line[-1]
                name = page_handler.persona_map[color]

                ut.show_persona_portrait(color, name, width=200)
                with st.expander(f"The {name}"):
                    st.write(f'"{quote.strip()}"')

        with col2:
            col2.subheader("How you might talk to the personalities you may misunderstand:")
            for y in misunderstand[:2]:
                line = y.split(':')
                color = line[0]
                quote = line[-1]
                name = page_handler.persona_map[color]

                ut.show_persona_portrait(color, name, width=200)
                with st.expander(f"The {name}"):
                    st.write(f'"{quote.strip()}"')

featured_people = Path(f"res/FeaturedPeople/{name_persona.lower()}s.png")
if featured_people.is_file():
    st.image(featured_people)
