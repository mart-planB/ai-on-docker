import streamlit as st
import requests

def generate_sales_email():
    st.title("AI Sales Email Generator")
    
    # Input fields
    customer_name = st.text_input("Customer Name")
    company = st.text_input("Company Name")
    product_interest = st.text_input("Product/Service of Interest")
    previous_interaction = st.text_area("Previous Interaction Details (if any)")
    
    style = st.select_slider(
        "Email Style",
        options=["Formal", "Professional", "Friendly", "Casual"]
    )
    
    if st.button("Generate Email"):
        prompt = f"""
        Generate a sales follow-up email with these details:
        - To: {customer_name} at {company}
        - Product/Service: {product_interest}
        - Previous Interaction: {previous_interaction}
        - Style: {style}
        
        Make it personalized, engaging, and focused on value proposition.
        Include a clear call to action.
        """
        
        response = requests.post("http://ollama:11434/api/generate", json={
            "model": "local-llama3",
            "prompt": prompt
        })
        
        st.text_area("Generated Email", response.json()["response"], height=300) 