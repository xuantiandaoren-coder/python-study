from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory

from memory.local_model import local_model

model = local_model()

prompt_template = ChatPromptTemplate.from_messages(
    [("system","你是一个助手，擅长能力{ability},用20个字以内回答，如果不知道的话，请回答“不知道”。"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human","{input}"),]
)


store = {}
chain = prompt_template | model
def get_session_history(session_id:str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)

r1 = chain_with_history.invoke({"ability":"数学","input":"勾股定理是啥"}, {'configurable': {'session_id': '[your-value-here]'}})
print(r1)
r2 = chain_with_history.invoke({"ability":"数学","input":"我刚才问了啥"}, {'configurable': {'session_id': '[your-value-here]'}})
print(r2)