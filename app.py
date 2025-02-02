import streamlit as st
import requests
import json

def load_knowledge_base():
    try:
        with open('knowledge_base.json', 'r') as f:
            return json.load(f)
    except:
        return {"error": "Knowledge base not accessible"}

st.title("Customer Support Assistant")
st.markdown("Ask questions about our products, pricing, or get help with issues.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask a question..."):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate and display assistant response
    with st.chat_message("assistant"):
        try:
            knowledge = load_knowledge_base()
            message_lower = prompt.lower()
            
            # Check knowledge base for relevant info
            knowledge_info = ""
            if "pricing" in message_lower:
                knowledge_info = f"Pricing information: {json.dumps(knowledge.get('pricing', {}))}"
            elif "feature" in message_lower:
                knowledge_info = f"Features information: {json.dumps(knowledge.get('features', {}))}"
            elif any(issue in message_lower for issue in ["problem", "issue", "help"]):
                knowledge_info = f"Common issues: {json.dumps(knowledge.get('common_issues', {}))}"
            else:
                knowledge_info = "No specific information found."

            enhanced_prompt = f"""
            Context: You are a customer service representative for our company.
            Knowledge Base Info: {knowledge_info}
            
            Customer Question: {prompt}
            
            Please provide a helpful, accurate response using the knowledge provided.
            """
            
            response = requests.post("http://ollama:11434/api/generate", json={
                "model": "local-llama3",
                "prompt": enhanced_prompt,
                "temperature": 0.7,
                "stream": False
            })
            
            if response.status_code == 200:
                assistant_response = response.json().get("response", "No response received")
                st.markdown(assistant_response)
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
            else:
                st.error(f"Error: API returned status code {response.status_code}")
                
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Add example questions as buttons
st.sidebar.markdown("### Example Questions")
if st.sidebar.button("What are your pricing plans?"):
    st.chat_input("What are your pricing plans?")
if st.sidebar.button("Tell me about the features in the pro plan"):
    st.chat_input("Tell me about the features in the pro plan")
if st.sidebar.button("How do I fix login issues?"):
    st.chat_input("How do I fix login issues?") 