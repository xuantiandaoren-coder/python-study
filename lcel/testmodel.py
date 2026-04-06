from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from lcel.local_model import local_model

prompt = ChatPromptTemplate.from_template(
    "Tell me a short joke about {topic}"
)

output_parser = StrOutputParser()

model = local_model()

chain = ({"topic":RunnablePassthrough()}
    | prompt | model | output_parser
)

print(chain.invoke("ice cream"))