import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI,OpenAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

load_dotenv()
print(os.getenv("OPENAI_API_KEY"))
llm = ChatOpenAI(temperature=0,model="deepseek-chat")
respone = llm.invoke("WHO are you")
print(respone)

messages=[
    SystemMessage(content="你是知识渊博的专家，知道很多著名书籍相关的只是，请简短的用20个子回答问题"),
    HumanMessage(content="我的身份是学员，我的名字是小于"),
    SystemMessage(content="欢迎，有什么需要咨询的？"),
    HumanMessage(content="三国志介绍的什么事情"),
    SystemMessage(content="三国志介绍的是东汉的历史"),
    HumanMessage(content="红楼梦呢"),
]

response = llm.invoke(messages)
print(response)






















# ERROR

# llm = OpenAI(temperature=0,model="deepseek-chat")
# llm.invoke("Who are you")

