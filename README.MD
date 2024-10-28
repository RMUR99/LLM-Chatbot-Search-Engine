
LLM Chatbot Search Engine  🔎🤖
This project showcases Streamlit ang langchain library to create a chatbot that is able to search the internet from sources like Arvix , Wikipedia and DuckDuckDuckGo 🦆while also using GROQ API key for AI Service 
Before starting you need to : 
-	Get your GROQ API KEY (Free) 🔑
-	Install Dependencies ( will be provided in the repo ) ⚙️
-	Please make sure not to share your Key with anyone ! 🔑
-	The project will work on your own API Key but you may change it in the sidebar in the setting menu if needed ⚙️
As you go through the project you will see 
-	Imports 
-	Environment variables (where you set the API Keys ) 
-	API Wrappers and tools ( Which does queries for ArXiv and Wikipedia to fetch the top result , and sets Duck Duck Go Tool) 
-	StreamLit Interface
-	Sidebar setting  for API key 
-	Chat Message management ( which sets the history of  the messages session) 
-	User Input handling (this is will show the text in the chatbot and it will append to the user input) 
-	- Setting up Chat Agent ( initializes Groq Model with the provided API Key along the search tools 
-	Displaying Responses (this is initialize text based on the chat history , and uses `Callback Handler` in order to manage the output 

