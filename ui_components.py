import streamlit as st

def setup_page():
    st.set_page_config(page_title="Instant Land AI (Gemini)", layout="wide")
    st.title("🏛️ Intelligent Land Records Assistant (PostgreSQL Edition)")

def render_sidebar():
    with st.sidebar:
        st.header("🌐 Language Settings")
        target_lang = st.selectbox(
            "Secondary Language:",
            ["Kannada", "Hindi", "Telugu", "Tamil"],
            index=0
        )
        st.divider()
        st.caption("Using Google Gemini 1.5 Flash (Free Tier)")
        st.caption("Powered by PostgreSQL & PGVector")
        return target_lang

def display_results(response, target_lang):
    if not response:
        return

    if "---" in response:
        eng, sec = response.split("---", 1)
    else:
        eng, sec = response, "Translation unavailable."

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🇬🇧 English")
        st.info(eng.replace("ENGLISH:", "").strip())
    with col2:
        st.subheader(f"🌐 {target_lang}")
        st.success(sec.replace(f"{target_lang.upper()}:", "").strip())
    
    # --- FOOTER ---
    st.divider()
    st.caption("Extracted from Government Circulars via PostgreSQL.")
