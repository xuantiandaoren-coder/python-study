from langchain_core.prompts import ChatPromptTemplate

from memory.local_model import local_model

model = local_model()

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个乐于助人的助手，尽你所能回答所有问题。"),
        ("user","{question}")
    ]
)

chain = prompt_template | model
print(chain.invoke({"question": "你好，我是小于，请问金庸是谁"}))
print(chain.invoke({"question": "你好，我是谁"}))