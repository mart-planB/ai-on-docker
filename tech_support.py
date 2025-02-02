import streamlit as st
import requests

def analyze_error():
    st.title("Technical Support Assistant")
    st.markdown("Get expert analysis and solutions for technical issues")
    
    error_message = st.text_area("Error Message")
    system_info = st.text_area("System Information")
    steps_taken = st.text_area("Steps Already Taken")
    
    if st.button("Analyze Issue"):
        if error_message and system_info:  # Basic validation
            prompt = f"""
            As a technical support specialist, analyze this issue:
            
            Error Message: {error_message}
            System Information: {system_info}
            Steps Already Taken: {steps_taken}
            
            Provide:
            1. Root cause analysis
            2. Step-by-step solution
            3. Prevention tips
            """
            
            try:
                response = requests.post("http://ollama:11434/api/generate", json={
                    "model": "local-llama3",
                    "prompt": prompt,
                    "stream": False
                })
                
                if response.status_code == 200:
                    analysis = response.json().get("response", "No response received")
                    st.markdown("### Analysis and Solution")
                    st.write(analysis)
                else:
                    st.error(f"Error: API returned status code {response.status_code}")
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.warning("Please provide both error message and system information")

if __name__ == "__main__":
    analyze_error() 