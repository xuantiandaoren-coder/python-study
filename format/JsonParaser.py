from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from common.local_model import local_model

llm = local_model()

template= """
你是一个助手，需要返回用户信息的json格式数据
{format_instructions}

请返回一个包含以下字段的JSON对象：
- name:用户的姓名
- age:用户的年龄
- hobbies:用户的爱好列表
- favorite_color:用户最喜欢的颜色

用户信息：{text}
"""

paraser = JsonOutputParser()

prompt_template=PromptTemplate(
    template=template,
    input_variables=["text"],
    partial_variables={"format_instructions": paraser.get_format_instructions()}
)

prompt = prompt_template.format_prompt(text="用户叫张三，年龄25岁，喜欢阅读、游泳和编程，最喜欢的颜色是蓝色")
print("prompt:",prompt)

resp = llm.invoke(prompt)
print(type(resp))
print("resp:",resp)

output=paraser.invoke(resp)
print(output)