from langchain_community.agent_toolkits.powerbi import prompt
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda

from lcel.local_model import local_model

model = local_model()
prompt_template = ChatPromptTemplate.from_template(
    "Tell me a short joke about {topic}"
)
# resp = model.invoke(prompt_template.invoke({"topic":"icream"}))

chain = prompt_template | model | RunnableLambda(func=lambda x: print(x))
chain.invoke({"topic":"icream"})
# print(chain.invoke({"topic":"icream"}))

