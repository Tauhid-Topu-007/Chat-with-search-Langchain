# 🔎 Chat with Search — LangChain

An AI-powered web search chatbot built with **Streamlit, LangChain, LangGraph, and Groq**. Ask questions in natural language and let the agent decide when to search the web or retrieve encyclopedic information from Wikipedia.

The repository also includes a Jupyter notebook exploring LangChain tools and agents, arXiv research search, and a Retrieval-Augmented Generation (RAG) workflow using FAISS and OpenAI embeddings.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/LangChain-Agents-1C3C3C?logo=langchain&logoColor=white" alt="LangChain">
  <img src="https://img.shields.io/badge/LLM-Groq-F55036" alt="Groq">
</p>

## ✨ Features

- **Conversational interface:** Chat with the assistant through a Streamlit application.
- **Live web search:** Uses DuckDuckGo search to retrieve web results for current topics.
- **Wikipedia lookup:** Uses the Wikipedia tool for general and encyclopedic information.
- **Tool-using AI agent:** LangGraph's prebuilt ReAct agent selects and invokes tools based on the user's question.
- **Groq-powered inference:** Uses the `openai/gpt-oss-120b` model through Groq.
- **Streaming-capable model configuration:** The Groq chat model is configured with streaming enabled.
- **Visible agent activity:** Streamlit callback handling displays tool/agent activity in the chat interface.
- **Session chat history:** Keeps messages in Streamlit session state during the active session.
- **Notebook learning examples:** Includes experiments with Wikipedia, arXiv, custom retrieval tools, FAISS, and agent execution.

## 🧰 Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| User interface | Streamlit |
| LLM provider | Groq |
| Chat model | `openai/gpt-oss-120b` |
| Agent orchestration | LangGraph |
| LLM integration | LangChain |
| Web search | DuckDuckGo Search (`ddgs`) |
| Knowledge lookup | Wikipedia |
| Notebook vector store | FAISS |
| Notebook embeddings | OpenAI Embeddings |
| Configuration | python-dotenv |

## 🏗️ Architecture

```text
                         ┌────────────────────────┐
                         │       User             │
                         │  Enters a question     │
                         └───────────┬────────────┘
                                     │
                                     ▼
                         ┌────────────────────────┐
                         │   Streamlit Chat UI    │
                         │  app.py + chat history │
                         └───────────┬────────────┘
                                     │
                                     ▼
                         ┌────────────────────────┐
                         │       Groq LLM         │
                         │   openai/gpt-oss-120b  │
                         └───────────┬────────────┘
                                     │
                                     ▼
                         ┌────────────────────────┐
                         │   LangGraph ReAct      │
                         │        Agent           │
                         └───────────┬────────────┘
                                     │
                       Chooses a tool when needed
                          ┌──────────┴──────────┐
                          ▼                     ▼
                ┌─────────────────┐   ┌─────────────────┐
                │ DuckDuckGo      │   │ Wikipedia       │
                │ Web Search      │   │ Knowledge Tool  │
                └────────┬────────┘   └────────┬────────┘
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌────────────────────────┐
                         │ Agent processes results│
                         │ and prepares an answer │
                         └───────────┬────────────┘
                                     │
                                     ▼
                         ┌────────────────────────┐
                         │  Response in Streamlit │
                         └────────────────────────┘
```

### How the application works

1. The user submits a question through Streamlit's chat input.
2. The application checks for a Groq API key.
3. The question is passed to the LangGraph ReAct agent.
4. The agent can call DuckDuckGo for web results or Wikipedia for encyclopedic information.
5. The model uses the returned tool output to prepare a response.
6. The assistant's response is added to the current Streamlit session history.

## 📁 Project Structure

```text
Chat-with-search-Langchain/
│
├── app.py                 # Streamlit chatbot and LangGraph agent
├── tools_agents.ipynb     # Notebook: tools, agents, arXiv and RAG examples
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignore rules
└── README.md              # Project documentation
```

## ⚙️ Getting Started

### 1. Prerequisites

- Python 3.10 or newer
- pip
- A Groq API key

Create or access your API key from the [Groq Console](https://console.groq.com/keys).

### 2. Clone the repository

```bash
git clone https://github.com/Tauhid-Topu-007/Chat-with-search-Langchain.git
cd Chat-with-search-Langchain
```

### 3. Create a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

Streamlit will provide a local URL (normally [http://localhost:8501](http://localhost:8501)).

### 6. Add your Groq API key

1. Open the application in your browser.
2. Find **Settings** in the sidebar.
3. Paste your Groq API key into **Enter your Groq API Key**.
4. Start asking questions in the chat input.

> **Security:** The current app accepts the Groq key through a password-type Streamlit sidebar field. Never commit API keys, tokens, or other secrets to GitHub.

## 💬 Example Questions

- `What is retrieval-augmented generation (RAG)?`
- `What are the latest developments in large language models?`
- `Explain the transformer architecture.`
- `Who developed the Python programming language?`
- `Compare LangChain and LangGraph.`
- `Find recent research about computer vision.`

The agent chooses whether to use web search or Wikipedia based on the question.

## 📓 Notebook: Tools, Agents & RAG

The `tools_agents.ipynb` notebook contains additional hands-on experiments beyond the Streamlit app:

- Creating and using the Wikipedia query tool.
- Searching research papers with the arXiv integration.
- Loading web pages with LangChain's `WebBaseLoader`.
- Splitting documents with `RecursiveCharacterTextSplitter`.
- Generating embeddings with `OpenAIEmbeddings`.
- Creating a FAISS vector store and retriever.
- Turning a retriever into a custom LangChain tool.
- Connecting tools to a Groq chat model.
- Building and running a tool-calling agent.

### Notebook environment variables

Some notebook examples use external API credentials. Configure the relevant keys in your local environment before running those cells:

- `GROQ_API_KEY` — for Groq model calls.
- `OPENAI_API_KEY` — for the OpenAI embeddings example.

Do not paste real credentials into notebook cells before committing or sharing the notebook. Prefer environment variables or a local `.env` file excluded from version control.

## 🔐 Environment & API Keys

The Streamlit application currently asks for the Groq API key in its sidebar, so a `.env` file is not required to run the app.

For notebook experiments that use environment variables, you can create a local `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
```

Keep `.env` out of version control. Do not use placeholder values as real credentials.

## 🛠️ Troubleshooting

### Missing Groq API key

If the app asks you to add a Groq API key, enter a valid key in the sidebar settings.

### Dependency installation problems

Upgrade pip and retry:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If a dependency fails to install, check that your Python version is supported by that package.

### Web search returns no results

The search tool retries DuckDuckGo using several regions. Search providers can still temporarily rate-limit or fail to return results. Try again with a more specific query.

### Wikipedia lookup errors

Wikipedia requests depend on an external service. Temporary network issues or rate limits may affect results.

## ⚠️ Current Scope & Notes

- The Streamlit app currently provides web search and Wikipedia tools.
- The arXiv and FAISS-based RAG examples are demonstrated in the notebook; they are not currently connected to the Streamlit app.
- Chat history is stored in Streamlit session state and is not a persistent database.
- Search results and generated answers may be incomplete or inaccurate. Verify important information using the original sources.
- The dependency file includes packages for several LangChain experiments; not every listed package is required by the Streamlit app itself.

## 🚀 Possible Future Improvements

- Add source links and clearer citations to answers.
- Add arXiv search as an application tool.
- Add document upload and PDF-based RAG.
- Add persistent chat history and conversation management.
- Add configurable LLM model selection.
- Add improved error handling, retries, and search-result validation.
- Add automated tests and deployment instructions.

## 👨‍💻 Author

**Tauhidul Islam Topu**

- GitHub: [@Tauhid-Topu-007](https://github.com/Tauhid-Topu-007)
- LinkedIn: [Tauhidul Islam Topu](https://www.linkedin.com/in/tauhidul-islam-topu-1a04b31ab/)
- Portfolio: [tauhid-topu](https://portfolio-frontend-rust-six.vercel.app/)

## 📄 License

No license file is currently included in this repository. Unless a license is added, the project remains under the default copyright terms; check with the author before redistributing or reusing it.

---

<p align="center">
  Built with ❤️ using Python, LangChain, LangGraph, Streamlit, and Groq.
</p>
