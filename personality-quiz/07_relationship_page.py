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

        # relation_image = "res/BlogImageTest.png"
        # # relation_image = "res/BlogImageMOBILETest.png"
        # st.text(relation_image)
        # st.image(relation_image)

        fond_of = data[color_persona]["Fond Of"]
        misunderstand = data[color_persona]["May Have Trouble Understanding"]

        #st.title(f'Your Result: The {top2_rename[0]}!')
        persona_image1 = f'res/test_{color_persona.lower()}.png'
        favor_image = f'res/relationships/{name_persona.lower()}_favors.png'
        #st.image(persona_image1, width=400)
        st.image(favor_image)

        # Section for "Get Along With" personalities

        col1, col2 = st.columns(2)
        with col1:
            col1.subheader("How you might talk to the personalities you get along with:")
            for x in fond_of:
                line = x.split(':')
                color = line[0]
                quote = line[-1]
                name = page_handler.persona_map[color]
                
                # with st.expander(f"The {name}"):
                    # col1, col2 = st.columns([1, 2])
                    # with col1:
                    #     im = f'res/test_{color.lower()}.png'
                    #     st.image(im, width=200)
                    # with col2:
                    #     # quotes had some leading whitespace
                    #     st.write(f'"{quote.strip()}"')

                im = f'res/test_{color.lower()}.png'
                st.image(im, width=200)
                with st.expander(f"The {name}"):
                    st.write(f'"{quote.strip()}"')

        with col2:
            # Section for "May Have Trouble Understanding" personalities
            col2.subheader("How you might talk to the personalities you may misunderstand:")
            for y in misunderstand[:2]:
                line = y.split(':')
                color = line[0]
                quote = line[-1]
                name = page_handler.persona_map[color]
                
                # with st.expander(f"The {name}"):
                    # col1, col2 = st.columns([1, 2])
                    # with col1:
                    #     im = f'res/test_{color.lower()}.png'
                    #     st.image(im, width=200)
                    # with col2:
                    #     st.write(f'"{quote}"')
                im = f'res/test_{color.lower()}.png'
                st.image(im, width=200)
                with st.expander(f"The {name}"):
                    st.write(f'"{quote.strip()}"')


with st.container(border=True):

    with st.form('page_form'):
        # Buttons section
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
