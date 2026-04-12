from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from memory.local_model import local_model

model = local_model()

prompt_template = ChatPromptTemplate.from_messages(
    [("system","你是一个热于助人的助手，尽你所能回答所有问题，简洁回复，20个字左右"),
    MessagesPlaceholder(variable_name="messages"),
    ("user","{question}"),]

)

chain = prompt_template | model

print(chain.invoke({
    "messages": [
        HumanMessage(content="将这句话翻译成英文：我喜欢编程"),
        AIMessage(content="I love  progamming"),
    ],
    "question": "我刚才说了什么？"
}).content)

