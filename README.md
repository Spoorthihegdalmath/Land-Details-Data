# 🏛️ Intelligent Land Records Assistant (PostgreSQL Edition)

An AI-powered chatbot designed to assist with Karnataka land records queries. It uses **Google Gemini 1.5 Flash** for reasoning and **PostgreSQL (PGVector)** for efficient document retrieval.

## 🚀 Features
- **AI-Powered Q&A**: Answers queries about land rules, conversion, and regulations.
- **Bilingual Support**: Provides answers in **English** and a selected regional language (**Kannada, Hindi, Telugu, Tamil**).
- **RAG Architecture**: Uses Retrieval-Augmented Generation to ground answers in official government circulars.
- **PostgreSQL Vector Search**: Scalable document storage and retrieval using `pgvector`.

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **LLM**: Google Gemini 1.5 Flash
- **Embeddings**: HuggingFace (`all-MiniLM-L6-v2`)
- **Database**: PostgreSQL + PGVector
- **Framework**: LangChain

## 📂 Project Structure
```
Chatbot Details Fetching/
├── app.py                # Main application entry point
├── config.py             # Configuration and environment variables
├── database.py           # Database connection and PGVector setup
├── models.py             # AI model initialization (LLM & Embeddings)
├── chatbot_logic.py      # Core logic for processing queries
├── ui_components.py      # UI layout and components
├── requirements.txt      # Python dependencies
└── .env                  # Environment variables (API keys & DB creds)
```

## ⚙️ Setup & Installation

### 1. Prerequisites
- Python 3.10+
- PostgreSQL installed and running.
- `pgvector` extension enabled in PostgreSQL.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file in the root directory:
```ini
GOOGLE_API_KEY=your_google_api_key_here
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
DB_HOST=localhost
DB_NAME=postgres
DB_USER=postgres
DB_PASS=password
DB_PORT=5432
```

### 4. Database Setup
Ensure your PostgreSQL database is running. The application assumes the `vector` extension is enabled.
```sql
CREATE EXTENSION vector;
```
*(Note: Previous migration scripts handled the initial data population)*

## ▶️ Running the Application
```bash
streamlit run app.py
```

## 📝 License
[MIT](https://choosealicense.com/licenses/mit/)
