# 003-tutorial.py
# LangChain Tutorial: Generic Tools

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain.schema import HumanMessage

# Load environment variables
load_dotenv()

# Initialize our language model
# Note: 'gpt-4o-mini' is not an official OpenAI model name. This may cause an error.
llm = ChatOpenAI(model="gpt-4o-mini")

# Define a simple function to use as a tool
def get_current_weather(location):
    # This is a mock function. In a real scenario, you'd call an actual weather API
    return f"The weather in {location} is currently sunny and 22°C.\n"

# Create a generic tool
tools = [
    Tool(
        name="Weather Checker",
        func=get_current_weather,
        description="Useful for getting the current weather in a specific location"
    )
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
    "Answer the following question: {question}"
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
        "question": "What's the weather like in Tokyo?"
    })

    print("Answer:")
    print(result['output'])

if __name__ == "__main__":
    main()