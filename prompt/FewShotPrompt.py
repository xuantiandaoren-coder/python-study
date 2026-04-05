from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate
from common.local_model import local_model

model = local_model()

exapmles=[
    {"input":"北京天气怎么样","output":"北京市"},
    {"input":"南京是江苏的","output":"南京市"},
    {"input":"武汉有什么好吃的","output":"武汉市"}
     ]
    

example_prompt = PromptTemplate(
    input_variables=["input","output"],
    template="输入：{input}\n,输出:{output}"
)

few_shot_prompt = FewShotPromptTemplate(
    examples = exapmles,
    example_prompt = example_prompt,
    prefix = "请回答下面问题:",
    suffix="输入:{input}\n 输出:",
    input_variables=["input"]
)

prompt = few_shot_prompt.format(input="烟花三月下扬州")
print(prompt)
print(model.invoke(prompt).content)