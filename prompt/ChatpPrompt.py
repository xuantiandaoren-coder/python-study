from langchain_core.prompts import ChatPromptTemplate
from common.local_model import local_model

template = ChatPromptTemplate(
    [
        ("system", "You are a helpful AI bot. Your name is {name}."),
        ("human", "Hello, how are you doing?"),
        ("ai", "I'm doing well, thanks!"),
        ("human", "{user_input}"),
    ]
)


prompt = template.invoke({"name":"joke","user_input":"please add 1+1 ?"})
# prompt = template.from_messages(name="joke",user_input="")


print(prompt.to_json)

# llm = local_model()

# print(llm.invoke(prompt).content)