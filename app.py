from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="تحلیل ریت و کامنت‌های کافه‌بازار — جاباما",
    page_icon="⭐",
    layout="wide",
)

st.markdown(
    """
    <style>
    #MainMenu, header, footer {visibility: hidden;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    [data-testid="stAppViewContainer"] {background: #FBFAF7;}
    iframe {display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).with_name("dashboard.html").read_text(encoding="utf-8")
components.html(html, height=5800, scrolling=True)
