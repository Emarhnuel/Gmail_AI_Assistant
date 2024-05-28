import os
import streamlit as st
from langchain_community.agent_toolkits import GmailToolkit
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from io import StringIO
import json

# Load environment variables
load_dotenv()

# Sidebar for uploading credentials.json
st.sidebar.title("Configuration")
credentials_file = st.sidebar.file_uploader("Upload credentials.json", type="json")

# Sidebar for OpenAI API Key
openai_api_key = st.sidebar.text_input("Enter your OPENAI_API_KEY", type="password")

# Sidebar for selecting OpenAI model
model_options = ["gpt-3.5-turbo", "gpt-4-turbo"]
selected_model = st.sidebar.selectbox("Choose OpenAI model", model_options)

# Check if the credentials file is uploaded
if credentials_file is not None:
    credentials = json.load(credentials_file)
    st.sidebar.success("credentials.json uploaded successfully")
else:
    st.sidebar.error("Please upload credentials.json")


# Check if the OpenAI API Key is provided
if openai_api_key:
    st.sidebar.success("OpenAI API Key provided")
else:
    st.sidebar.error("Please provide the OpenAI API Key")

# Instantiate GmailToolkit with the credentials
if credentials_file is not None and openai_api_key:
    toolkit = GmailToolkit(credentials=credentials)
    # Get tools
    tools = toolkit.get_tools()


    # Set up the LLM and agent
    instructions = "You are an assistant and you are very good at managing my emails."
    base_prompt = hub.pull("langchain-ai/openai-functions-template")
    prompt = base_prompt.partial(instructions=instructions)
    llm = ChatOpenAI(model=selected_model, temperature=0, openai_api_key=openai_api_key)
    agent = create_openai_functions_agent(llm, tools, prompt)

    def main():
        # Initialize Streamlit app
        st.title("Chat to your Gmail")

        # Initialize session state for messages
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display previous messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Handle new user input
        if prompt := st.chat_input("Ask your question:"):
            # Append user input to the messages and display it
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Prepare the input for the agent executor
            agent_input = {
                "input": prompt
            }

            # Invoke agent executor and get response
            agent_executor = AgentExecutor(
                agent=agent,
                tools=tools,
                verbose=False,
            )
            response = agent_executor.invoke(agent_input)

            # Append the response to the messages and display it
            st.session_state.messages.append({"role": "assistant", "content": response['output']})
            with st.chat_message("assistant"):
                st.markdown(response['output'])

    if __name__ == "__main__":
        main()

else:
    st.warning("Please upload credentials.json and provide the OpenAI API Key to proceed.")
