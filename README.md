User types message
       ↓
st.session_state.input_text updated
       ↓
on_change → handle_input() called
       ↓
st.session_state.messages.append(user message)
       ↓
LLM invoked → response
       ↓
st.session_state.messages.append(assistant message)
       ↓
st.session_state.input_text = "" (input cleared)
       ↓
Script reruns automatically
       ↓
Messages displayed in chat container
       ↓
Back to waiting for next user input
