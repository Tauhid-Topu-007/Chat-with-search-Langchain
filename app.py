import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langgraph.prebuilt import create_react_agent
import os
from dotenv import load_dotenv

# --- Wikipedia User-Agent fix (prevents JSONDecodeError / rate limiting) ---
import wikipedia
wikipedia.set_user_agent("my-streamlit-agent/1.0 (t.topu021@gmail.com)")
# ---------------------------------------------------------------------------

load_dotenv()

# Wikipedia Tool
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)

# DuckDuckGo Search Tool
search = DuckDuckGoSearchRun(name="Search")

st.title("🔎 Chat with search")

# Sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
    ]

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

# Chat input
if prompt := st.chat_input(placeholder="What is machine learning?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    if not api_key:
        st.info("Please add your Groq API key to continue.")
        st.stop()

    # Create the model
    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="openai/gpt-oss-120b",
        streaming=True
    )

    # Define tools (Arxiv removed to avoid version conflict)
    tools = [search, wiki]

    # Create the agent
    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt="You are a helpful assistant that can search the web and Wikipedia."
    )

    # Invoke the agent and display response
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        result = agent.invoke(
            {"messages": [{"role": "user", "content": prompt}]},
            config={"callbacks": [st_cb]}
        )
        response = result["messages"][-1].content
        st.session_state.messages.append({'role': 'assistant', "content": response})
        st.write(response)