import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_core.tools import Tool
from langgraph.prebuilt import create_react_agent
from ddgs import DDGS
import os
from dotenv import load_dotenv

# --- Wikipedia User-Agent fix (prevents JSONDecodeError / rate limiting) ---
import wikipedia
wikipedia.set_user_agent("my-streamlit-agent/1.0 (contact@example.com)")
# ---------------------------------------------------------------------------

load_dotenv()

# Wikipedia Tool
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)


# --- Robust DuckDuckGo Search with region retry ---
def robust_ddg_search(query: str) -> str:
    regions = ["us-en", "uk-en", "de-de", "wt-wt"]
    for region in regions:
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, region=region, max_results=3))
                if results:
                    formatted = []
                    for r in results:
                        title = r.get("title", "")
                        body = r.get("body", "")
                        href = r.get("href", "")
                        formatted.append(f"{title}\n{body}\n{href}")
                    return "\n\n".join(formatted)
        except Exception:
            continue
    return "No results found after retrying with multiple regions."


search = Tool(
    name="Search",
    func=robust_ddg_search,
    description="Useful for searching the web for current information. Input should be a search query string."
)
# ---------------------------------------------------

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

    # Define tools
    tools = [search, wiki]

    # Create the agent
    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt="You are a helpful assistant that can search the web and Wikipedia. "
               "Use the Search tool for current information and the Wikipedia tool for encyclopedic facts."
    )

    # Invoke the agent and display response
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        try:
            result = agent.invoke(
                {"messages": [{"role": "user", "content": prompt}]},
                config={"callbacks": [st_cb]}
            )
            response = result["messages"][-1].content
        except Exception as e:
            response = f"Sorry, I encountered an error while processing your request: {str(e)}"
        st.session_state.messages.append({'role': 'assistant', "content": response})
        st.write(response)