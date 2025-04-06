import streamlit as st
import os
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOllama
from langchain.memory import ConversationBufferMemory
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

# ---- Page config ---- #
st.set_page_config(page_title="Bionova Chatbot", layout="wide")

# ---- Custom Styling ---- #
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .stChatMessage {
            border-radius: 12px !important;
            padding: 10px 15px;
            margin-bottom: 10px;
        }
        .stChatMessage.user {
            background-color: #e8f5e9;
            text-align: right;
        }
        .stChatMessage.assistant {
            background-color: #f1f8e9;
        }
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .css-1y4p8pa {display: none;} /* Hide sidebar if user tries to reopen */
    </style>
""", unsafe_allow_html=True)

# ---- Title ---- #
st.title("🌳 Bionova Chatbot")
st.caption("💬 An intelligent assistant powered by Ollama + LangChain")

# ---- Fixed Config ---- #
MODEL = "mistral"
MAX_HISTORY = 3
CONTEXT_SIZE = 8192

# ---- Session State Setup ---- #
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "memory" not in st.session_state or st.session_state.get("prev_context_size") != CONTEXT_SIZE:
    st.session_state.memory = ConversationBufferMemory(return_messages=True)
    st.session_state.prev_context_size = CONTEXT_SIZE

# ---- LangChain Components ---- #
llm = ChatOllama(model=MODEL, streaming=True)
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
retriever = vectorstore.as_retriever(search_type="similarity")
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="map_reduce", retriever=retriever, return_source_documents=True)

# ---- Chat History Display ---- #
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---- Memory Trim ---- #
def trim_memory():
    while len(st.session_state.chat_history) > MAX_HISTORY * 2:
        st.session_state.chat_history.pop(0)

# ---- Chat Input ---- #
if prompt := st.chat_input("Ask me your question here…"):
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    trim_memory()

    with st.chat_message("assistant"):
        response_container = st.empty()
        retrieved_docs = retriever.get_relevant_documents(prompt)
        
        full_response = (
            "❌ No relevant documents found." if not retrieved_docs
            else qa({"query": prompt}).get("result", "🤖 No answer generated.")
        )

        response_container.markdown(full_response)
        st.session_state.chat_history.append({"role": "assistant", "content": full_response})
        trim_memory()