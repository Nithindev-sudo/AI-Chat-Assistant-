# import streamlit as st
# from langchain_ollama import ChatOllama


# a = ChatOllama(
#     model="llama-3.2-3b-it:latest",
# )


# user_input = st.text_input("User Input", "text")

# response = a.invoke(user_input)
# st.write(response.content)
 
import streamlit as st
from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama-3.2-3b-it:latest",
)


if "messages" not in st.session_state:
    st.session_state.messages = []

if "input_text" not in st.session_state:
    st.session_state.input_text = ""

# ---------------------------
# Function to handle user input
# ---------------------------
def handle_input():
    user_input = st.session_state.input_text.strip()
    if user_input:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Get LLM response
        response = llm.invoke(user_input)

        # Add assistant message
        st.session_state.messages.append({"role": "assistant", "content": response.content})

        # Clear input box
        st.session_state.input_text = ""


st.title("Simple Chatbot")

# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")

# Text input with callback
st.text_input(
    "Ask anything:",
    key="input_text",
    on_change=handle_input
)

# Optional: Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []

