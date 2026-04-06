from langchain_core.example_selectors import LengthBasedExampleSelector
from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate
# from prompt.common.local_model import local_model

examples = [

    {"input":"快乐","output":"悲伤"},
    {"input":"高","output":"矮"},
    {"input":"精力充沛","output":"昏昏欲睡"},
    {"input":"阳光","output":"阴暗"},
    {"input":"喧哗","output":"安静"},
]
 


example_prompt = PromptTemplate(
    input_variables=["input","output"],
    template="input:{input}\n output:{output}",
)

example_selector = LengthBasedExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    max_length=50,
    get_text_length=lambda x:len(x) # 计算文本长度函数
)
dynamic_prompt = FewShotPromptTemplate(
    example_selector = example_selector,
    example_prompt = example_prompt,
    suffix="input:{input}\n output",
    input_variables=["input"],
)

short_questions = "大"
prompt = dynamic_prompt.invoke({"input":short_questions})
print(prompt)