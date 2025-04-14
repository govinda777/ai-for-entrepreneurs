import streamlit as st
from streamlit_chatbox import ChatBox

def render_chat():
    """
    Renders a chatbox component for AI interactions
    """
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Create chat container
    st.subheader("Assistente IA")
    
    # Initialize chatbox
    chatbox = ChatBox(key="chat_component")
    
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        chatbox.message(message["content"], author=message["role"])
    
    # Process input
    if prompt := st.chat_input("Digite sua pergunta..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        chatbox.message(prompt, author="user")
        
        # Here would be the AI processing logic
        # For now, just echo back a response
        response = f"Você perguntou: {prompt}\n\nEsta funcionalidade será implementada em breve."
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        # Display assistant response in chat message container
        chatbox.message(response, author="assistant") 