from langchain_core.output_parsers import StrOutputParser

from common.local_model import local_model
model = local_model()
parser = StrOutputParser()

prompt = "讲一句笑话"
rsp = model.invoke(prompt)
print(type(rsp))
print(rsp)

parase_rsp = parser.invoke(rsp)
print(parase_rsp)