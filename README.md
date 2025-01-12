# Chatbot_SQL
I've developed a SQL-based chatbot that allows users to make queries to a personal database using natural language. The chatbot returns query results also in natural language. To achieve this, I've used advanced techniques such as Retrieval-Augmented Generation (RAG) and Prompt Engineering.

For the implementation, I used the following Python files:
- **[backend.py](https://github.com/cuaudrup/Chatbot_SQL/blob/main/backend.py)**: In this file, I defined my own prompt and, using an OpenAI GPT-4 Mini LLM, I created the chatbot infrastructure to execute queries on the database and retrieve the data.
- **[frontend.py](https://github.com/tu_usuario/cuaudrup/Chatbot_SQL/main/frontend.py)**: For the user interface, I used Streamlit to create a user-friendly chat interface that allows users to easily make queries.

