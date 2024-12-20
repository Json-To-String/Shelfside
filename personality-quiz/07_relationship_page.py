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

        #st.title(f'Your Result: The {top2_rename[0]}!')
        persona_image1 = f'res/test_{color_persona.lower()}.png'
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

                im = f'res/test_{color.lower()}.png'
                st.image(im, width=200)
                with st.expander(f"The {name}"):
                    st.write(f'"{quote.strip()}"')

        with col2:
            col2.subheader("How you might talk to the personalities you may misunderstand:")
            for y in misunderstand[:2]:
                line = y.split(':')
                color = line[0]
                quote = line[-1]
                name = page_handler.persona_map[color]

                im = f'res/test_{color.lower()}.png'
                st.image(im, width=200)
                with st.expander(f"The {name}"):
                    st.write(f'"{quote.strip()}"')

with st.container(border=True):

    try:
        st.image(f"res/FeaturedPeople/{name_persona.lower()}s.png")
    except:
        st.header("People in the industry you're like")
        st.text("<< Coming Soon! >>")

with st.container(border=True):

    with st.form('page_form'):
        col1, col2 = st.columns(2)
        with col1:
            results = st.form_submit_button(f"⏪ Back to results!",
                                            use_container_width=True, type='primary')
            if results:
                st.switch_page('personality-quiz/06_results_page.py')
        with col2:
            recommend = st.form_submit_button(f"3 games for you! ⏩",
                                            use_container_width=True, type='primary')
            if recommend:
                st.switch_page('personality-quiz/08_recommend_page.py')
