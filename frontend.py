# Run with: streamlit run frontend.py in the terminal.
import streamlit as st
import backend

# Custom CSS for global styling
st.markdown(
    """
    <style>
        body {
            background-color: #001f3d;
            color: white;
        }
        .user-message {
            background-color: #ffc107;
            color: black;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            font-size: 16px;
        }
        .assistant-message {
            background-color: #333333;
            color: white;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            font-size: 16px;
        }
        div.stTextInput {
            position: fixed;
            bottom: 80px;
            left: 10%;
            width: 80%;
            margin: 0 auto;
            background-color: #222222;
            border-radius: 10px;
            padding: 10px;
            border: 1px solid #ffc107;
            color: white;
            font-size: 16px;
        }
        div.stTextInput label {
            color: white;  /* Make label text white */
        }
        div.stButton > button {
            position: fixed;
            bottom: 20px;
            left: 10%;
            background-color: #ffc107;
            color: black;
            border: none;
            border-radius: 10px;
            padding: 15px;
            width: 80%;
            font-size: 16px;
            cursor: pointer;
        }
        div.stButton > button:hover {
            background-color: #e6ac00;
        }
        .css-1l269bu.e1fqkh3o3 {
            margin-top: 50px;
        }
        h1 {
            color: #000000;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Set the title
st.title("🤖 SQL Chatbot: DS Market")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input with white-colored label
user_question = st.text_input("💬 Ask a question about predicted sales:")

# Process the user input
if st.button("Submit") and user_question.strip():
    try:
        # Generate SQL query
        query = backend.write_query(user_question)  # Replace with your implementation
        
        # Execute the query
        result = backend.execute_query(query)  # Replace with your implementation
        
        # Generate the assistant's response in natural language
        answer = backend.generate_answer(user_question, query, result)  # Replace with your implementation
        
        # Add user and assistant messages to the chat history
        st.session_state.chat_history.append(("user", user_question))
        st.session_state.chat_history.append(("assistant", answer))  # Only display the answer
    
    except Exception as e:
        st.session_state.chat_history.append(("assistant", f"⚠️ **Error:** {str(e)}"))

# Display the chat history
for role, message in st.session_state.chat_history:
    if role == "user":
        st.markdown(
            f"""
            <div class="user-message">
                <b>🧑‍💻 User:</b> {message}
            </div>
            """, unsafe_allow_html=True
        )
    elif role == "assistant":
        st.markdown(
            f"""
            <div class="assistant-message">
                <b>🤖 Assistant:</b> {message}
            </div>
            """, unsafe_allow_html=True
        )

# Initial instruction for new users
if not st.session_state.chat_history:
    st.info("Hello! Ask me a question about predicted sales, and I'll assist you. 😊")
