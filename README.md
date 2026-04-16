# 💰 FinanceBot – Retrieval-Augmented Financial Education AI Assistant

## 🌟 Project Overview
FinanceBot is a Retrieval-Augmented Generation (RAG) based AI assistant designed to provide accurate and structured financial education. It retrieves verified information from trusted financial sources (such as SEC Investor.gov) and uses a Large Language Model (LLM) to generate clear, educational responses.

The system focuses on financial literacy, scam awareness, and investment education while ensuring responses are grounded in real documents rather than hallucinated content.

---

## ✨ Features
- 💬 AI-powered financial Q&A chatbot
- 📚 Retrieval-Augmented Generation (RAG) for grounded answers
- 🔍 Semantic search using FAISS + MMR (diversity-aware retrieval)
- 🧠 Multi-topic financial knowledge base (scams, crypto, AI fraud, investing tips)
- 💡 Structured response generation (Answer → Explanation → Key Points → Example → Sources)
- 💬 Multi-turn conversation memory
- ⚠️ Built-in financial safety guardrails (no investment advice or predictions)
- 🖥️ Streamlit-based interactive chat interface

---

## 🚀 Technologies Used

**Backend / Core AI:**
- Python
- LangChain
- Groq API (LLaMA 3-70B)
- HuggingFace SentenceTransformers (MiniLM embeddings)

**Retrieval System:**
- FAISS Vector Database
- MMR (Maximal Marginal Relevance) Retriever

**Data Processing:**
- BeautifulSoup (web scraping)
- Requests
- Regex (text cleaning)

---

## 🏗️ Architecture
Web Scraping (Investor.gov) → Data Cleaning → Text Chunking → Embedding Generation → FAISS Vector Store → MMR Retriever → Prompt Engineering → Groq LLM → Streamlit UI

---

## 📊 Data Collection
The dataset is built by scraping verified financial education content from SEC Investor.gov and related official financial literacy pages.

Topics include:
- Stock market scams
- Cryptocurrency fraud
- AI-driven financial scams
- Relationship investment scams
- Investment safety tips (2025)
- Account protection guidelines

---

## ✂️ Text Processing Pipeline
- HTML cleaning using BeautifulSoup
- Removal of scripts, headers, and navigation content
- Text normalization using regex
- Chunking using RecursiveCharacterTextSplitter:
  - chunk_size = 500
  - chunk_overlap = 50

Each chunk is stored as a LangChain Document with metadata (topic, source, chunk_id).

---

## 🔍 Vector Database (FAISS)
- Embedding Model: sentence-transformers/all-MiniLM-L6-v2
- Storage: FAISS vector index (locally saved)
- Retrieval Strategy:
  - MMR (Maximal Marginal Relevance)
  - Balances relevance and diversity of retrieved chunks

---

## 🤖 LLM (Large Language Model)
- Model: LLaMA 3 (70B via Groq API)
- Temperature: 0.3 (balanced factual + coherent responses)
- Max Tokens: 1024

---

## 🧾 Prompt Engineering
FinanceBot uses a structured system prompt that enforces:
- Direct answer first
- Explanation breakdown
- Key points in bullet format
- Real-world example (RM-based where relevant)
- Source attribution

Constraints:
- No financial advice
- No predictions
- No stock recommendations
- Must include educational disclaimer

---

## 🔗 RAG Pipeline Flow
Retriever → Relevant Document Chunks → Prompt Injection → LLM → Structured Response

Implementation:
create_retrieval_chain(
    retriever,
    create_stuff_documents_chain(llm, prompt)
)

---

## 💬 Conversation Memory
- Uses LangChain HumanMessage & AIMessage
- Stores last 5 conversation turns
- Supports contextual multi-turn Q&A

---

## 🧪 Evaluation
The system is evaluated using predefined financial questions to test:
- Answer accuracy
- Retrieval relevance
- Source grounding
- Disclaimer compliance

Evaluation topics include:
- Stock scams
- Crypto fraud
- AI financial fraud
- Investment tips

---

## 🖥️ How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Set API key:
GROQ_API_KEY=your_api_key

3. Run Streamlit app:
streamlit run app.py

---

## 📦 Project Structure
financebot-rag/
│── finance_dataset/        # scraped financial articles
│── finance_faiss_index/    # FAISS vector store
│── app.py                  # Streamlit chatbot UI
│── rag_pipeline.py        # RAG logic (retrieval + LLM)
│── requirements.txt
│── README.md

---

## ⚠️ Limitations
- Not a licensed financial advisor
- No real-time market data
- Limited to scraped dataset knowledge
- Context limited by chunk retrieval window

---

## 🔮 Future Improvements
- Real-time financial news API integration
- Hybrid retrieval (BM25 + FAISS)
- LangGraph-based memory system
- Better citation UI in Streamlit
- Deployment with authentication system

---

## 👨‍💻 Author
Developed as a Data Science / AI Engineering project focusing on:
- Retrieval-Augmented Generation (RAG)
- Financial NLP systems
- End-to-end LLM application design

---

## ⚠️ Disclaimer
This project is for educational purposes only and does not constitute financial advice.
