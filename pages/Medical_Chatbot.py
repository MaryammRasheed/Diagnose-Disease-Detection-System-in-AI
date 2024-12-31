import streamlit as st
from time import sleep
from utils.meditron import query_meditron  # Ensure the correct path and function exist

# App title
st.title("🤖 Medical Chatbot")
st.markdown("Ask health-related questions and get instant responses. Keep the conversation going!")

# Initialize session state for conversation history and input management
if "messages" not in st.session_state:
    st.session_state.messages = []
if "is_typing" not in st.session_state:
    st.session_state.is_typing = False  # Tracks whether the bot is "typing"

# Function to display chat history
def display_chat_history():
    for i, msg in enumerate(st.session_state.messages):
        # Alternate user and bot messages for better UI
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**Bot:** {msg['content']}")
    if st.session_state.is_typing:
        st.markdown("**Bot is typing...**")  # Simulate typing indicator

# Input field for user query
user_input = st.text_input("Your message:", key="input_field")

# Quick reply buttons
st.markdown("### Quick Suggestions:")
col1, col2, col3 = st.columns(3)
if col1.button("What are the symptoms of diabetes?"):
    user_input = "What are the symptoms of diabetes?"
if col2.button("What are the common flu treatments?"):
    user_input = "What are the common flu treatments?"
if col3.button("How to maintain a healthy diet?"):
    user_input = "How to maintain a healthy diet?"

# Process user input
if st.button("Send") and user_input:
    # Save user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Show typing indicator
    st.session_state.is_typing = True
    
    # Display chat history immediately
    display_chat_history()
    
    # Simulate delay and get bot response
    sleep(2)  # Simulate typing delay
    try:
        # Get bot response based on the entire conversation
        conversation_history = [msg["content"] for msg in st.session_state.messages]
        bot_response = query_meditron("\n".join(conversation_history))  # Pass full context to the bot
        
        # Save bot response to chat history
        st.session_state.messages.append({"role": "bot", "content": bot_response.strip()})
    except Exception as e:
        # Handle errors and log them
        bot_response = f"Error: {e}"
        st.session_state.messages.append({"role": "bot", "content": bot_response})
    finally:
        # Hide typing indicator
        st.session_state.is_typing = False

# Display chat history
display_chat_history()
