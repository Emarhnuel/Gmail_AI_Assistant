# Gmail_AI_Assistant

## Chat to your Gmail

This Streamlit application allows you to interact with your Gmail inbox using natural language queries. It leverages the power of OpenAI's language models and the Langchain framework to understand your requests and perform actions like searching, summarizing, and composing emails.

## Features

* **Natural Language Interface:** Ask questions about your emails in plain English.
* **Search:** Find specific emails based on sender, subject, or content.
* **Summarization:** Get concise summaries of email threads.
* **Compose:** Draft new emails or replies with assistance from the AI.

## Installation

1. **Clone the Repository:**
   ```
   git clone https://github.com/Emarhnuel/Gmail_AI_Assistant.git
   ```
   
2. **Install Dependencies:**
    ```
    pip install -r requirements.txt
    ```
   
## Usage

1. **Run the App:**
   ```
    streamlit run app.py
   ```
   
2. **load Credentials:**
    In the sidebar, upload your `credentials.json` file (obtained from Google Cloud Platform).

3. **Enter Open AI API Key:**
    Provide your OpenAI API key in the sidebar.

4. **Choose Model:**
    Select your preferred OpenAI model (e.g., gpt-3.5-turbo or gpt-4-turbo).

5. **Start Chatting:**
   Type your questions or requests in the chat input area.
