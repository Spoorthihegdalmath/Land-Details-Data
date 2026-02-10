import streamlit as st
from ui_components import setup_page, render_sidebar, display_results
from models import get_resources
from database import get_vector_store
from chatbot_logic import process_query

# --- UI SETUP ---
setup_page()

embeddings_model, llm_model = get_resources()

# --- LOAD VECTOR STORE ---
if "vector_db" not in st.session_state:
    st.session_state.vector_db = get_vector_store(embeddings_model)

vector_db = st.session_state.vector_db

# --- SIDEBAR ---
target_lang = render_sidebar()

# --- MAIN LOGIC ---
query = st.text_input(
    "Ask about land rules (English or Kannada):",
    placeholder="e.g., Explain the 3 gunta rule"
)

if query:
    if vector_db:
        response = process_query(query, vector_db, llm_model, target_lang)
        display_results(response, target_lang)
    else:
        st.error("❗ Vector database connection failed.")
