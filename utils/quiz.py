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


def show_error_summary(section: int, missing: list[int], focus: bool) -> None:
    count = len(missing)
    noun = "question" if count == 1 else "questions"
    links = "".join(
        f'<li><a href="#page{section}_question{i}-error">Question {i + 1}</a></li>'
        for i in missing
    )
    summary_id = f"quiz-errors-{section}"
    focus_summary = "true" if focus else "false"
    st.html(
        f"""
        <style>
        .quiz-error-summary {{
            border: 2px solid #b42318;
            border-radius: .5rem;
            padding: 1rem;
        }}
        .quiz-error-summary:focus {{
            outline: 3px solid currentColor;
            outline-offset: 3px;
        }}
        .quiz-error-summary h2 {{ font-size: 1.125rem; padding: 0; }}
        .quiz-error-summary a {{ display: inline-block; min-height: 24px; }}
        </style>
        <div class="quiz-error-summary" id="{summary_id}"
             role="region" aria-labelledby="{summary_id}-title" tabindex="-1">
            <h2 id="{summary_id}-title">Answer {count} more {noun} to continue</h2>
            <ul>{links}</ul>
        </div>
        <script>
        (() => {{
            const summary = document.getElementById("{summary_id}");
            if (!summary) return;
            if ({focus_summary}) summary.focus();
            const links = [...summary.querySelectorAll("a")];
            const connect = () => {{
                for (const link of links) {{
                    const id = link.getAttribute("href").slice(1);
                    const group = document.querySelector(
                        ".st-key-field_" + id.replace(/-error$/, "") + ' [role="radiogroup"]'
                    );
                    if (!group || !document.getElementById(id)) return false;
                    group.setAttribute("aria-describedby", id);
                    group.setAttribute("aria-invalid", "true");
                    group.onchange = () => {{
                        group.removeAttribute("aria-describedby");
                        group.removeAttribute("aria-invalid");
                    }};
                    link.onclick = event => {{
                        const radio = group.querySelector('input[type="radio"]');
                        if (!radio) return;
                        event.preventDefault();
                        radio.focus();
                    }};
                }}
                return true;
            }};
            if (connect()) return;
            // The summary can mount before the question widgets on a rerun.
            const observer = new MutationObserver(() => {{
                if (!summary.isConnected || connect()) observer.disconnect();
            }});
            observer.observe(document.body, {{childList: true, subtree: true}});
            setTimeout(() => observer.disconnect(), 2000);
        }})();
        </script>
        """,
        unsafe_allow_javascript=True,
    )


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
    summary = st.empty()

    handler.display_questions(section, show_errors=show_errors, answers=answers)
    missing = handler.unanswered_questions(section)
    if show_errors and missing:
        with summary.container():
            show_error_summary(section, missing, st.session_state.pop(f"{error_key}_focus", False))

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
        if missing:
            st.session_state[error_key] = True
            st.session_state[f"{error_key}_focus"] = True
            st.rerun()

        st.session_state[error_key] = False
        handler.store_answers(section)
        st.switch_page(next_page)
