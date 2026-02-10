import streamlit as st
from langchain_core.messages import HumanMessage

def process_query(query, vector_db, llm_model, target_lang):
    if not query:
        return

    with st.spinner("Gemini is analyzing your documents..."):
        try:
            # Perform similarity search
            raw_docs = vector_db.similarity_search(query, k=3)
            
            if not raw_docs:
                st.warning("No relevant documents found in the database. Please ensure migration is complete.")
                st.stop()
            
            context = "\n\n".join(d.page_content for d in raw_docs)

            prompt = f"""
You are a Karnataka land records expert.

RULES:
1. Preserve original Kannada legal terms if present.
2. Answer in TWO sections: English and {target_lang}.
3. Separate languages using '---'.

Context:
{context}

Question:
{query}

FORMAT:
ENGLISH:
---
{target_lang.upper()}:
"""

            res = llm_model.invoke(
                [HumanMessage(content=prompt)]
            ).content

            return res

        except Exception as e:
            st.error(f"Error during processing: {e}")
            return None
