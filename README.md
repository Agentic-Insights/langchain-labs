# 🤖 LangChain 101: Agentic AI Tutorial and Samples

Welcome to the LangChain 101 repository! This project serves as a beginner's tutorial and collection of samples for agentic work using LangChain, a powerful framework for building applications with large language models (LLMs).

## 📚 Overview

This repository is designed to provide a professional, ground-floor introduction to modern LangChain development, focusing on agentic AI applications. The examples and tutorials here use the latest LangChain APIs and best practices, ensuring you're learning with up-to-date and non-deprecated methods.

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.10+
- pip (Python package manager)

### Installation

1. Clone this repository: 
   ```
   git clone https://github.com/Agentic-Insights/langchain-labs
   cd langchain-labs
   ```
2. Create a conda environment (optional but recommended):
   ```
   conda create -n langchain-labs python=3.10
   conda activate langchain-labs
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## 📋 Requirements

- langchain
- langchain_openai
- python-dotenv
- openai

## 🗂️ Repository Structure

- `labs/`: Contains individual tutorial scripts and related files
- `utils/`: Helper functions and utility scripts
- `README.md`: This file, providing an overview of the repository

## 🎓 Tutorials

### Basics in Jupyter Notebooks / Google Colab


1. [**001-tutorial**](labs/001-tutorial.ipynb): Introduction to LangChain basics - [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Agentic-Insights/langchain-labs/blob/main/labs/001-tutorial.ipynb)
   - Set up your first LangChain environment
   - Learn how to initialize and use a language model
   - Explore basic interactions with the AI


2. [**002-tutorial**](labs/002-tutorial..ipynb): Working with prompt templates and RunnableSequence - [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Agentic-Insights/langchain-labs/blob/main/labs/002-tutorial.ipynb) 
   - Learn how to load prompts from external files
   - Understand and implement ChatPromptTemplates
   - Explore the concept of RunnableSequence for creating complex workflows\

### Tool Usage examples

3. [**003-tutorial**](labs/003-tutorial.py): Creating custom tools and agents
   - Implement a simple custom tool (Weather Checker)
   - Create a React agent using the custom tool
   - Understand how to combine prompts, tools, and agents

4. [**004-tutorial**](labs/004-tutorial.py): Using DuckDuckGo Search Tool
   - Integrate the DuckDuckGo search tool into your LangChain application
   - Learn how to create an agent that can perform web searches
   - Explore more complex prompt structures and agent interactions

5. [**005-tutorial-streamlit**](labs/005-tutorial-streamlit.py): Integrating Streamlit (With Error Handling)
   - Build a user-friendly web interface for your LangChain application using Streamlit
   - Implement error handling for more robust applications
   - Learn how to display intermediate steps and search processes to users

(More tutorials will be added as they are developed)

## 🛠️ Usage

Each tutorial in the `labs/` directory is a self-contained script. To run a tutorial:

1. Navigate to the `labs/` directory:
   ```
   cd labs
   ```

2. Run the desired tutorial script. For most tutorials:
   ```
   python 001-tutorial.py
   ```
   For the 005-tutorial which uses Streamlit:
   ```
   streamlit run 005-tutorial-streamlit.py
   ```

3. Follow the prompts or instructions provided by the tutorial script.

4. For tutorials that require API keys or other sensitive information, make sure to set up your `.env` file with the necessary credentials.

5. Some tutorials may require additional setup or resources. Always check the comments at the beginning of each script for any specific instructions.

6. To explore the code and understand how it works, open the tutorial scripts in your preferred code editor.

7. Feel free to modify the scripts and experiment with different parameters or inputs to deepen your understanding of LangChain concepts.

Remember to activate your virtual environment before running the tutorials if you're using one.

## 🔑 API Keys

To use OpenAI's models, you need to set up your API key. Create a `.env` file in the root directory and add your OpenAI API key:
