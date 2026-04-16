import streamlit as st
import os
from dotenv import load_dotenv

# LangChain
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

# -------------------------------
# 🔑 Load API Key
# -------------------------------
load_dotenv(".env.txt")
groq_api_key = os.getenv("GROQ_API_KEY")

# -------------------------------
# 🧠 Streamlit UI Setup
# -------------------------------
st.set_page_config(page_title="FinanceBot", layout="wide")
st.title("💰 FinanceBot")
st.write("Ask questions about finance, investing, or scams")

# -------------------------------
# 💾 Cache RAG system (important)
# -------------------------------
@st.cache_resource
def load_rag():
    # Load documents (your dataset folder)
    dataset_folder = "./finance_dataset"
    docs = []

    for file in os.listdir(dataset_folder):
        if file.endswith(".txt"):
            with open(os.path.join(dataset_folder, file), "r", encoding="utf-8") as f:
                text = f.read()
                docs.append(Document(
                    page_content=text,
                    metadata={"topic": file.replace(".txt", "")}
                ))

    # Split documents
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    splits = splitter.split_documents(docs)

    # Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Vector store
    vectorstore = FAISS.from_documents(splits, embeddings)

    # Retriever (MMR)
    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 4, "fetch_k": 20, "lambda_mult": 0.7}
    )

    # LLM (Groq)
    llm = ChatGroq(
        api_key=groq_api_key,
        model="llama3-70b-8192",
        temperature=0.3,
        max_tokens=1024,
    )

    # Prompt
    SYSTEM_PROMPT = """You are FinanceBot, an expert financial assistant.
Answer clearly using provided context only.
Always include sources.
End with: ⚠️ Educational purposes only."""

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ])

    # Chains
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    return rag_chain

rag_chain = load_rag()

# -------------------------------
# 🧠 Chat memory (Streamlit way)
# -------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -------------------------------
# 💬 Chat UI
# -------------------------------
user_input = st.chat_input("Ask something about finance...")

if user_input:
    # Display user message
    st.chat_message("user").write(user_input)

    # Call RAG
    result = rag_chain.invoke({
        "input": user_input,
        "chat_history": st.session_state.chat_history
    })

    answer = result["answer"]
    source_docs = result.get("context", [])

    sources = list({
        doc.metadata.get("topic", "Unknown")
        for doc in source_docs
    })

    # Display answer
    st.chat_message("assistant").write(answer)

    # Show sources
    with st.expander("📚 Sources"):
        st.write(", ".join(sources))

    # Save history
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("assistant", answer))

# -------------------------------
# 🔄 Reset button
# -------------------------------
if st.sidebar.button("Reset Chat"):
    st.session_state.chat_history = []