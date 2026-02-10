import streamlit as st
from langchain_postgres import PGVector
from config import VECTOR_DB_URL

# --- LOAD PGVECTOR ---
def get_vector_store(embeddings):
    try:
        vector_store = PGVector(
            embeddings=embeddings,
            collection_name="land_records",
            connection=VECTOR_DB_URL,
            use_jsonb=True,
        )
        return vector_store
    except Exception as e:
        st.error(f"❌ Database Connection Error: {e}")
        st.stop()
