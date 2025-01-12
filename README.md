# 🤖 Chatbot SQL DS Market
I've developed a SQL-based chatbot that allows users to make queries to a personal database using natural language. The chatbot processes the input query and returns results in natural language as well. To accomplish this, I utilized advanced techniques like Retrieval-Augmented Generation (RAG) and Prompt Engineering to enhance the chatbot's ability to understand and respond accurately.

Additionally, I incorporated Langchain, a powerful framework that facilitates the integration of language models with external data sources, making the query process more efficient and effective. Langchain helps manage the interaction between the natural language input, the model, and the database.

For secure management of my API keys, I used an .env file to load my OpenAI and Langchain API keys, ensuring that sensitive information is kept private and is not exposed in the codebase.

For the implementation, I used the following Python files:

- **[backend.py](https://github.com/cuaudrup/Chatbot_SQL/blob/main/backend.py)**: This file contains the core logic for defining the chatbot's prompt. Using an OpenAI GPT-4 Mini LLM, I created the infrastructure for the chatbot to execute queries on the database and retrieve data. The .env file is used to securely load my OpenAI and Langchain API keys, which are essential for the model's operation.
- **[frontend.py](https://github.com/tu_usuario/cuaudrup/Chatbot_SQL/main/frontend.py)**: This file handles the user interface, where I used Streamlit to create a simple and intuitive chat interface. Users can input their queries in natural language, and the chatbot will return responses directly within the interface, making it easy to interact with the system.

My database contains sales predictions for weeks 17 to 20 from a company called DS Market, a supermarket chain with over 3000 items per store. These stores are located across multiple cities, and the products are categorized into various departments. The LLM was used to query these sales predictions. This is where the chatbot's utility becomes clear, as it provides a practical way for people without technical SQL knowledge to quickly and easily access data from the database. Below are some example queries related to the database, where we have data on sales predictions and stock needs.

- First, here is what our Streamlit interface looks like for making the queries.

<div style="text-align: center;">
    <img src="https://github.com/cuaudrup/Chatbot_SQL/blob/main/images/Captura%20de%20pantalla%202025-01-12%20a%20las%2016.39.19.png" alt="Logo DS Market" />
</div>

<br><br>


- Here is an example of a query, where we ask for the top 5 best-selling products in New York during week 18.

<div style="text-align: center;">
    <img src="https://github.com/cuaudrup/Chatbot_SQL/blob/main/images/Captura%20de%20pantalla%202025-01-12%20a%20las%2016.41.55.png" alt="Logo DS Market" />
</div>



- In this example, we can see that it is able to sort categories by total sales.

<div style="text-align: center;">
    <img src="https://github.com/cuaudrup/Chatbot_SQL/blob/main/images/Captura%20de%20pantalla%202025-01-12%20a%20las%2016.48.16.png" alt="Logo DS Market" />
</div>



- As the last example, we have the stock requirements for a specific product across different weeks.

<div style="text-align: center;">
    <img src="https://github.com/cuaudrup/Chatbot_SQL/blob/main/images/Captura%20de%20pantalla%202025-01-12%20a%20las%2016.55.16.png" alt="Logo DS Market" />
</div>

I encourage you to try implementing tools like this with your own databases, as they can be very useful. I hope you enjoyed it, see you soon.
