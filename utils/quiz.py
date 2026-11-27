from functools import lru_cache

import streamlit as st

from utils.utils import Handler


SECTIONS = (
    ("Board gaming in general", "questions1_outside_game_night.txt"),
    ("How you approach a game", "questions2_during_games_mechanical.txt"),
    ("Playing with friends", "questions3_mechanical_sociala.txt"),
    ("Tricky game-night decisions", "questions4_mechanical_socialb.txt"),
    ("The social side of game night", "questions5_during_games_social.txt"),
)
SECTION_PAGES = tuple(
    f"personality-quiz/{section:02d}_question_page{section}.py"
    for section in range(1, len(SECTIONS) + 1)
)
START_PAGE = "personality-quiz/00_start_page.py"


@lru_cache
def question_count() -> int:
    total = 0
    for _, filename in SECTIONS:
        handler = Handler()
        handler.get_questions(f"personality-quiz/{filename}")
        total += len(handler.question_list)
    return total


def show_quiz_section(section: int, next_page: str) -> None:
    title, question_file = SECTIONS[section - 1]
    last_section = section == len(SECTIONS)
    previous_page = SECTION_PAGES[section - 2] if section > 1 else START_PAGE

    handler = Handler()
    handler.get_questions(f"personality-quiz/{question_file}")
    answers = st.session_state.setdefault("quiz_answers", {})
    error_key = f"page{section}_show_errors"

    if st.button("Back to start" if section == 1 else "Back"):
        st.switch_page(previous_page)

    st.title(title)
    progress = st.empty()
    show_errors = st.session_state.get(error_key, False)
    if show_errors and not handler.all_answered(section):
        st.error("Please answer all questions before continuing.")

    handler.display_questions(section, show_errors=show_errors, answers=answers)
    total = question_count()
    answered = sum(answer is not None for answer in answers.values())
    progress.progress(
        answered / total,
        text=f"Section {section} of {len(SECTIONS)} · {answered} of {total} answered",
    )

    if st.button(
        "See my result" if last_section else "Continue",
        width="stretch",
        type="primary",
    ):
        if not handler.all_answered(section):
            st.session_state[error_key] = True
            st.rerun()

        st.session_state[error_key] = False
        handler.store_answers(section)
        st.switch_page(next_page)
