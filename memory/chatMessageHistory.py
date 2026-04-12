from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory

from memory.local_model import local_model

model = local_model()

prompt_template = ChatPromptTemplate.from_messages(
    [("system","你是一个热于助人的助手，尽你所能回答所有问题，简洁回复，20个字左右"),
    MessagesPlaceholder(variable_name="messages"),
    ("user","{question}"),]

)

chat_message_history = ChatMessageHistory()
chat_message_history.add_user_message("将这句话翻译成英文：我喜欢编程")
chat_message_history.add_ai_message("I love  progamming")
chain = prompt_template | model

print(chain.invoke({
    "messages": chat_message_history.messages,
    "question": "我刚才说了什么？"
}).content)
