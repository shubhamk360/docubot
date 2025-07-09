import streamlit as st
from document_loader import load_documents
from agents import MultiAgentPipeline
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["USER_AGENT"] = os.getenv("USER_AGENT", "docubot")

st.set_page_config(page_title="DocuBot", layout="wide")
st.title("📄 DocuBot: Multi-Source Document Chat")

# Initialize session state
if "docs" not in st.session_state:
    st.session_state["docs"] = []
if "pipeline" not in st.session_state:
    st.session_state["pipeline"] = None
if "last_source" not in st.session_state:
    st.session_state["last_source"] = ""

# Clear session button
if st.button("🧹 Clear Session"):
    st.session_state.clear()
    st.markdown("<script>location.reload()</script>", unsafe_allow_html=True)

# Inputs
uploaded_files = st.file_uploader(
    "Upload PDF, DOCX, or Image", 
    type=["pdf", "docx", "jpg", "jpeg", "png"], 
    accept_multiple_files=True
)
url = st.text_input("Or enter a YouTube/Web URL")

# Process Uploaded Files
if uploaded_files and st.button("💡 Process Uploaded Files"):
    st.session_state.clear()
    st.session_state["last_source"] = "file"
    try:
        docs = load_documents(files=uploaded_files, url=None)
        if not docs:
            st.warning("Uploaded files had no readable text.")
        else:
            st.session_state["docs"] = docs
            st.success(f"✅ Loaded {len(docs)} documents from files.")
            st.markdown("<script>location.reload()</script>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"❌ File load failed: {e}")
        st.stop()

# Auto-load new URL
if url and url != st.session_state.get("last_source"):
    st.session_state.clear()
    st.session_state["last_source"] = url
    with st.spinner("🌐 Loading from URL..."):
        try:
            docs = load_documents(files=None, url=url)
            if not docs:
                st.warning("No content found at the URL.")
            else:
                st.session_state["docs"] = docs
                st.success("✅ Loaded content from URL.")
                st.markdown("<script>location.reload()</script>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"❌ URL load failed: {e}")
            st.stop()

# Build fresh pipeline
if st.session_state.get("docs"):
    try:
        st.session_state["pipeline"] = MultiAgentPipeline(st.session_state["docs"])
    except Exception as e:
        st.error(f"❌ Pipeline initialization failed: {e}")
        st.stop()

# Ask a question
if st.session_state.get("pipeline"):
    mode = st.selectbox("Select Agent", ["Summarize + Critique", "Explain like I'm 5", "Direct Answer"])
    question = st.text_input("Ask a question:")
    if question:
        with st.spinner("🤖 Generating..."):
            try:
                answer = st.session_state["pipeline"].run(question, mode=mode)
                st.markdown(f"### 🤖 Response:\n{answer}")
            except Exception as e:
                st.error(f"❌ Failed to generate response: {e}")
