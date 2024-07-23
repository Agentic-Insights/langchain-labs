# 005-tutorial-streamlit.py
# LangChain Tutorial: Integrating Streamlit (With Error Handling)

import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor
from langchain.schema import OutputParserException

# Load environment variables
load_dotenv()

# Initialize our language model
llm = ChatOpenAI(model="gpt-4o-mini")

# Create the DuckDuckGo search tool
search = DuckDuckGoSearchRun()

# Create a list with the DuckDuckGo search tool
tools = [
    DuckDuckGoSearchRun(name="Web Search")
]

# Function to load prompt from file
@st.cache_resource
def load_prompt_template(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Load the React prompt template from file
react_prompt_template = load_prompt_template('tutorial.react-prompt.md')

# Create the PromptTemplate
react_prompt = PromptTemplate.from_template(react_prompt_template)

# Create the agent
agent = create_react_agent(llm, tools, react_prompt)

# Create an agent executor with error handling
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True, 
    return_intermediate_steps=True,
    handle_parsing_errors=True 
)

# Create a prompt template for the main query
prompt = ChatPromptTemplate.from_template(
    "Answer the following question using the most up-to-date information you can find: {question}"
)

# Create our RunnableSequence
@st.cache_resource
def create_sequence():
    return RunnableSequence(
        prompt,
        lambda prompt_result: agent_executor.invoke({
            "input": prompt_result.to_messages()[0].content,
            "tools": tools,
            "tool_names": ", ".join([tool.name for tool in tools]),
            "agent_scratchpad": ""
        })
    )

sequence = create_sequence()

# Streamlit UI
st.title("AI Assistant with Web Search")

# User input
user_question = st.text_input("What would you like to know?")

if user_question:
    try:
        with st.spinner("Searching for an answer..."):
            # Use the sequence
            result = sequence.invoke({"question": user_question})
            
            # Display the answer
            st.subheader("Answer:")
            st.write(result['output'])

        # Display the search process
        with st.expander("See the search process"):
            if 'intermediate_steps' in result:
                for step in result['intermediate_steps']:
                    st.write(f"Action: {step[0]}")
                    st.write(f"Observation: {step[1]}")
                    st.write("---")
            else:
                st.write("No intermediate steps available.")

    except OutputParserException as e:
        st.error(f"An error occurred while processing your request: {str(e)}")
        st.write("The AI generated a response, but it didn't follow the expected format. Here's what it said:")
        st.write(e.llm_output)

    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")

# Add a footer
st.markdown("---")
st.markdown("Powered by LangChain and Streamlit")