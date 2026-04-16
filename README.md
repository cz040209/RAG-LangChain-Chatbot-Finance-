🌟 Project Overview

FinanceBot is an intelligent Retrieval-Augmented Generation (RAG) AI assistant designed to provide accurate, structured, and educational financial guidance.

It retrieves verified financial knowledge from trusted investor education sources (such as the SEC Investor.gov) and generates well-structured, easy-to-understand explanations using a Large Language Model (LLM).

Unlike generic chatbots, FinanceBot ensures responses are:

Grounded in real financial documents
Structured for learning
Free from hallucinated financial advice

The system is designed for financial literacy, scam awareness, and investment education.

✨ Features
💬 Intelligent Financial Q&A

Ask questions about scams, investing, crypto risks, and financial safety.

📚 Retrieval-Augmented Generation (RAG)

Answers are generated using real financial documents retrieved from a vector database.

🔍 Semantic Search (FAISS + MMR)

Efficient retrieval of relevant document chunks using:

FAISS vector similarity search
Maximal Marginal Relevance (MMR) for diverse results
🧠 Multi-Source Knowledge Base

Covers verified topics such as:

Stock scams
Crypto fraud & custody risks
AI-powered financial scams
Relationship investment scams
Investment safety tips
💡 Structured Response Generation

Responses follow a strict format:

Direct Answer
Explanation
Key Points
Real-world Example (RM-based)
Source Attribution
💬 Conversational Memory

Supports multi-turn conversation using chat history tracking.

⚠️ Financial Safety Guardrails
No financial advice
No stock predictions
No personalized investment recommendations
🚀 Technologies Used
🧠 AI / LLM Stack
Groq API (LLaMA 3-70B)
LangChain (RAG orchestration)
HuggingFace Transformers (Embeddings)
🔎 Retrieval System
FAISS (Vector Database)
SentenceTransformers (MiniLM embeddings)
MMR Retriever (diversity-aware search)
🌐 Data Pipeline
BeautifulSoup (web scraping)
Requests (HTTP data fetching)
Regex (text cleaning)
🖥️ Frontend
Streamlit (chat UI)
🐍 Backend / Core
Python 3
LangChain Core modules
dotenv (API key management)

