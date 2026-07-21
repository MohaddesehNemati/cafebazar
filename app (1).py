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

HERE = Path(__file__).parent
CANDIDATES = [
    HERE / "dashboard.html",
    HERE / "streamlit-app" / "dashboard.html",
    Path.cwd() / "dashboard.html",
]

html_path = next((p for p in CANDIDATES if p.exists()), None)

if html_path is None:
    st.error(
        "فایل dashboard.html پیدا نشد. آن را دقیقاً کنار app.py (در ریشهٔ ریپو) "
        "آپلود کنید و سپس از منوی Manage app گزینهٔ Reboot را بزنید."
    )
    st.stop()

html = html_path.read_text(encoding="utf-8")
components.html(html, height=5800, scrolling=True)
