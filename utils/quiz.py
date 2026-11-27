import streamlit as st

from utils.utils import Handler


SECTIONS = (
    ("Let’s start with some questions about board gaming in general…", "questions1_outside_game_night.txt", 0),
    ("Now it’s time for game night! What is your mental approach?", "questions2_during_games_mechanical.txt", 20),
    ("Let’s throw your friends in the mix and see how you answer!", "questions3_mechanical_sociala.txt", 40),
    ("Ok! Now let’s make the questions trickier for the home stretch!", "questions4_mechanical_socialb.txt", 60),
    (
        "Almost there! We’ll end with 5 questions solely about hanging out with your friends on game night.",
        "questions5_during_games_social.txt",
        100,
    ),
)


def show_quiz_section(section: int, next_page: str) -> None:
    title, question_file, progress = SECTIONS[section - 1]
    last_section = section == len(SECTIONS)

    st.title(title)
    st.progress(progress, text=f"Page {section}/{len(SECTIONS)}")

    handler = Handler()
    handler.get_questions(f"personality-quiz/{question_file}")

    error_key = f"page{section}_show_errors"
    show_errors = st.session_state.get(error_key, False)
    if show_errors:
        st.error("Please answer all questions before continuing.")

    with st.form("page_form"):
        handler.display_questions(section, show_errors=show_errors)
        submitted = st.form_submit_button(
            "Calculate My Results!" if last_section else "Submit",
            width="stretch",
            type="primary",
        )

    if submitted:
        if not handler.all_answered(section):
            st.session_state[error_key] = True
            st.rerun()

        st.session_state[error_key] = False
        handler.store_answers(section)
        st.switch_page(next_page)
