# 004-tutorial.py
# LangChain Tutorial: Using DuckDuckGo Search Tool

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor

# Load environment variables
load_dotenv()

# Initialize our language model
# Note: 'gpt-4o-mini' is not an official OpenAI model name. This may cause an error.
llm = ChatOpenAI(model="gpt-4o-mini")

# Create the DuckDuckGo search tool
search = DuckDuckGoSearchRun()

# Create a list with the DuckDuckGo search tool
tools = [
    DuckDuckGoSearchRun(name="Web Search")
]

# Function to load prompt from file
def load_prompt_template(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Load the React prompt template from file
react_prompt_template = load_prompt_template('tutorial.react-prompt.md')

# Create the PromptTemplate
react_prompt = PromptTemplate.from_template(react_prompt_template)

# Create the agent
agent = create_react_agent(llm, tools, react_prompt)

# Create an agent executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Create a prompt template for the main query
prompt = ChatPromptTemplate.from_template(
    "Answer the following question using the most up-to-date information you can find: {question}"
)

# Create our RunnableSequence
sequence = RunnableSequence(
    prompt,
    lambda prompt_result: agent_executor.invoke({
        "input": prompt_result.to_messages()[0].content,
        "tools": tools,
        "tool_names": ", ".join([tool.name for tool in tools]),
        "agent_scratchpad": ""
    })
)

def main():
    # Use the sequence
    result = sequence.invoke({
        "question": "What are the latest developments in artificial intelligence?"
    })

    print("Answer:")
    print(result['output'])

if __name__ == "__main__":
    main()