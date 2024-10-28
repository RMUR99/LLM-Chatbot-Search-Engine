import streamlit as st 
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun , WikipediaQueryRun , DuckDuckGoSearchRun 
from langchain.agents import initialize_agent , AgentType 
from langchain.callbacks import StreamlitCallbackHandler
import os 
from dotenv import load_dotenv 
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

## first add Arxiv and wikipedia tools 
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1 , doc_content_chars_max= 200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)
api_wrapper = WikipediaAPIWrapper(top_k_results= 1 , doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)
search = DuckDuckGoSearchRun(name = "Search")

#preparing the interface 
st.title("Langchain Chat + Search Engine 🔎")
"""
using `SteamlitCllbackHandler` used to display thoughts and action of an agent in an interactive streamlit app
"""

#side bar for setting 
st.sidebar.title("Settings ⚙️" )
api_key = st.sidebar.text_input("Enter your Groq API key " , type = "password")
if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant" , "content":" HI :) I am a chatbot that uses web to search what do you want to search ?"}
    ]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

if prompt:= st.chat_input(placeholder="what is machine learning?"):
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)

    llm = ChatGroq(groq_api_key= api_key , model_name = "llama3-8b-8192" , streaming= True)
    tools = [search , arxiv , wiki]

    search_agent = initialize_agent( tools , llm , agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION , handling_parsing_errors = True)

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages , callbacks=[st_cb])
        st.session_state.messages.append({'role':'assistant' , "contnet":response})
        st.write(response)

