import streamlit as st
import requests
import json

st.title("Local LLama3 Chat Interface")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What's your message?"):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate and display assistant response
    with st.chat_message("assistant"):
        try:
            response = requests.post("http://ollama:11434/api/generate", json={
                "model": "local-llama3",
                "prompt": prompt,
                "stream": False  # Add this to get a complete response
            })
            
            if response.status_code == 200:
                try:
                    response_data = response.json()
                    # Handle different response formats
                    if "response" in response_data:
                        assistant_response = response_data["response"]
                    elif "content" in response_data:
                        assistant_response = response_data["content"]
                    else:
                        assistant_response = str(response_data)  # Fallback to showing raw response
                except json.JSONDecodeError:
                    assistant_response = "Error: Invalid response format from API"
            else:
                assistant_response = f"Error: API returned status code {response.status_code}"
                
            st.markdown(assistant_response)
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
            
        except requests.exceptions.RequestException as e:
            error_message = f"Error connecting to Ollama: {str(e)}"
            st.error(error_message) 