# 📄 DocuBot — Multi-Source AI Document Chatbot 

**DocuBot** is an AI-powered multi-agent RAG (Retrieval-Augmented Generation) chatbot built with **LangChain**, **Cohere**, **Gemini**, and **Streamlit**.

Upload documents (`PDF`, `DOCX`), images (`JPG`, `PNG`), or even YouTube/Web URLs — then **ask anything** and let custom agents **summarize**, **critique**, or **explain** in simple terms.

---

##  **Features**

 **Multi-source ingestion**
-  Upload PDF, DOCX
-  OCR for images (JPG, PNG)
-  YouTube videos (captions or description)
-  Web pages (with custom User-Agent)

**Multi-agent reasoning**
-  Direct Answer agent
-  Summarize & Critique agent
-  Explain Like I’m 5 agent

 **Powered by**
- LangChain (`Community`, `Cohere`, `Gemini`)
- Chroma vector store
- Cohere embeddings + Gemini LLM
- PyMuPDF, pytesseract, pytube, yt-dlp for versatile content parsing

---

##  **Tech Stack**

- [Streamlit](https://streamlit.io/) — beautiful interactive UI
- [LangChain](https://python.langchain.com/) — RAG pipeline
- [Cohere](https://cohere.com/) — fast embeddings
- [Gemini](https://deepmind.google) — Google’s next-gen LLM
- [PyMuPDF, python-docx, pytesseract, PIL] — local parsing & OCR
- [pytube, yt-dlp] — robust YouTube caption fallback


