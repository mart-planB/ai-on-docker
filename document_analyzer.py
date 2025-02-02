import streamlit as st
import requests
from PyPDF2 import PdfReader
import docx

def extract_text(uploaded_file):
    if uploaded_file.type == "application/pdf":
        pdf = PdfReader(uploaded_file)
        text = " ".join(page.extract_text() for page in pdf.pages)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(uploaded_file)
        text = " ".join(paragraph.text for paragraph in doc.paragraphs)
    return text

def analyze_document():
    st.title("Document Analysis Assistant")
    
    uploaded_file = st.file_uploader("Upload your document (PDF/DOCX)", type=["pdf", "docx"])
    
    if uploaded_file:
        text = extract_text(uploaded_file)
        
        analysis_type = st.selectbox(
            "What would you like to do?",
            ["Summarize", "Extract Key Points", "Find Action Items", "Identify Risks"]
        )
        
        if st.button("Analyze"):
            prompt = f"""
            Document content: {text[:2000]}...
            
            Task: {analysis_type}
            Please provide a detailed {analysis_type.lower()} of this document.
            Focus on the most important information and present it in a clear format.
            """
            
            response = requests.post("http://ollama:11434/api/generate", json={
                "model": "local-llama3",
                "prompt": prompt
            })
            
            st.write(response.json()["response"])

if __name__ == "__main__":
    analyze_document() 