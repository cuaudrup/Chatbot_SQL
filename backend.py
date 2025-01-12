import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_community.tools.sql_database.tool import QuerySQLDatabaseTool
from langchain import hub
from typing_extensions import TypedDict, Annotated

load_dotenv()

# Configure environment variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"
openai_api_key = os.getenv("OPENAI_API_KEY")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not configured. Check your .env file.")
if not langchain_api_key:
    raise ValueError("LANGCHAIN_API_KEY is not configured. Check your .env file.")

# Load the database
db = SQLDatabase.from_uri("sqlite://///DSMarket.db")

# Create the LLM model
llm = ChatOpenAI(model="gpt-4o-mini")

class QueryOutput(TypedDict):
    """Generated SQL query."""
    query: Annotated[str, ..., "Syntactically valid SQL query."]

class State(TypedDict):
    question: str
    query: str
    result: str
    answer: str

# Function to generate the SQL query
def write_query(question: str):
    """Generate SQL query to fetch information using a custom prompt."""
    # Define the custom prompt with the provided information
    custom_query_prompt = f"""
    You are an expert SQL assistant with additional knowledge about the structure of the `id` column in the database. The `id` column follows a specific format:

    Example: SUPERMARKET_3_090_NYC_3

    The format is as follows:
    1. The text before the first underscore (`_`) is the **category** (e.g., SUPERMARKET).
    2. The number after the first underscore (`_`) is the **subcategory number** (e.g., 3).
    3. The number between the second and third underscores (`_`) is the **product number** (e.g., 090).
    4. The letters between the third and fourth underscores (`_`) are the **city abbreviation**, with the following mappings:
       - NYC: New York City
       - BOS: Boston
       - PHI: Philadelphia
    5. The number after the fourth underscore (`_`) is the **store number** within the city (e.g., 3).

    When processing queries, ensure you interpret the `id` column correctly based on these rules. For example:
    - A query asking for "all products in New York City" should filter by the city abbreviation `NYC`.
    - A query asking for "all products in category SUPERMARKET and subcategory 3" should filter by the respective category and subcategory.

    Rules for SQL generation:
    1. Only provide the SQL query, without explanations.
    2. Ensure the query is valid for SQLite.
    3. Use double quotes for column and table names if necessary.
    4. Do not include a semicolon (`;`) at the end of the query.

    Database Schema:
    {db.get_table_info()}

    User Question: {question}
    """

    try:
        # Ensure the input is a string
        structured_llm = llm.with_structured_output(QueryOutput)
        result = structured_llm.invoke(custom_query_prompt.strip())  # Pass only the string
        return result["query"]
    except Exception as e:
        raise ValueError(f"Error generating query: {str(e)}")

# Function to execute the SQL query
def execute_query(query: str):
    """Execute SQL query."""
    execute_query_tool = QuerySQLDatabaseTool(db=db)
    return execute_query_tool.invoke(query)

# Function to generate an answer from the result
def generate_answer(question: str, query: str, result: str):
    """Answer question using retrieved information as context."""
    prompt = (
        "Given the following user question, corresponding SQL query, "
        "and SQL result, answer the user question.\n\n"
        f'Question: {question}\n'
        f'SQL Query: {query}\n'
        f'SQL Result: {result}'
    )
    response = llm.invoke(prompt)
    return response.content
