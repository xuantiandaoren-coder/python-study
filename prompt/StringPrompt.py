from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from common.local_model import local_model


promptTemplate = PromptTemplate.from_template("tell me a joke about{topic}")
model = local_model()
prompt = promptTemplate.invoke({"topic":"rabit"})
response = model.invoke(prompt)
print(response)