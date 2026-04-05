import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
print(os.getenv("OPENAI_API_KEY"))
llm = ChatOpenAI(temperature=0,model="deepseek-chat")
respone = llm.invoke("WHO are you")
print(respone)
