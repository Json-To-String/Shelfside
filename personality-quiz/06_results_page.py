from collections import defaultdict
import json

import altair as alt
import pandas as pd
import streamlit as st

from utils.utils import Handler, show_persona_portrait


handler = Handler()
scores = defaultdict(float)
for section in range(1, 5):
    for color, score in st.session_state[f"page{section}_results"].items():
        scores[color] += score

top_colors = sorted(scores, key=scores.get, reverse=True)[:2]
primary, secondary = top_colors
primary_name, secondary_name = (handler.persona_map[color] for color in top_colors)
st.session_state["Top2"] = top_colors
st.session_state["Top2_rename"] = [primary_name, secondary_name]

with open("personality-quiz/personas0.json", encoding="utf-8") as file:
    persona = json.load(file)[primary]
with open("personality-quiz/color_combos0.json", encoding="utf-8") as file:
    secondary_blurb = json.load(file)[primary][secondary]

st.title(f"Your result: The {primary_name}")
st.markdown(persona["Blurb"])

if st.button("See my game recommendations", width="stretch", type="primary"):
    st.switch_page("personality-quiz/08_recommend_page.py")
if st.button("Explore friends & rivals", width="stretch"):
    st.switch_page("personality-quiz/07_relationship_page.py")

show_persona_portrait(primary, primary_name, width=320)

st.header("Strengths")
st.markdown("\n".join(f"- {strength}" for strength in persona["Strengths"]))

st.header("Weaknesses")
st.markdown("\n".join(f"- {weakness}" for weakness in persona["Weaknesses"]))

st.header(f"Quotes from a {primary_name}")
for quote in persona["Quotes"][:3]:
    st.markdown(f"> {quote}")

st.header("Game-night habits")
attributes = [
    "How often will host game night",
    "How frequently will research a new game",
    "How often is a sore loser",
    "How often to come up with a wacky, unheard of strategy",
]
st.markdown("\n".join(f"- **{attribute}** · {persona[attribute]}" for attribute in attributes))

st.header(f"Your second match: The {secondary_name}")
st.markdown(secondary_blurb)

st.header("Your personality scores")
ranked_scores = sorted(scores, key=scores.get, reverse=True)
score_table = pd.DataFrame(
    [(handler.persona_map[color], scores[color]) for color in ranked_scores],
    columns=["Personality", "Score"],
)
chart = alt.Chart(score_table).mark_bar(stroke="#222222", strokeWidth=1).encode(
    y=alt.Y("Personality:N", sort=score_table["Personality"].to_list(), title=None),
    x=alt.X("Score:Q"),
    color=alt.Color(
        "Personality:N",
        scale=alt.Scale(
            domain=list(handler.persona_map.values()),
            range=list(handler.hex_colors.values()),
        ),
        legend=None,
    ),
    tooltip=["Personality:N", alt.Tooltip("Score:Q", format=".2f")],
).properties(height=300)
st.altair_chart(chart, width="stretch", theme=None)
with st.expander("View personality scores as text"):
    st.markdown("\n".join(
        f"- **{name}** · {score:g}"
        for name, score in score_table.itertuples(index=False, name=None)
    ))
