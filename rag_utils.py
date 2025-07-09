from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import uuid

def get_qa_chain(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(docs)

    if not texts:
        raise ValueError("❌ No usable text chunks found.")

    embeddings = CohereEmbeddings(
        cohere_api_key=os.getenv("COHERE_API_KEY"),
        model="embed-english-v3.0",
        user_agent=os.getenv("USER_AGENT", "docubot")
    )

    vectordb = Chroma.from_documents(
        documents=texts,
        embedding=embeddings,
        collection_name=f"docubot_{uuid.uuid4()}",
        persist_directory=None
    )
    retriever = vectordb.as_retriever()

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
