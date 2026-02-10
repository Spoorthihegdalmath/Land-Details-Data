import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings

# --- CACHE ONLY SAFE OBJECTS ---
@st.cache_resource
def get_resources():
    # Local embeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Gemini Model
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    
    return embeddings, llm
