from pydoc import text

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda,RunnablePassthrough
#group1
prompt_template=(
    PromptTemplate.from_template("tell me a joke about {topic}") + ",need simple, less than 10 setence"
    +"\n\n use{language} say"
)

print(prompt_template.invoke({"topic":"rabbit","language":"english"}))

#group2
full_template="""{introduction}
{example}
{start}
"""

full_prompt_template = PromptTemplate.from_template(full_template)

introduction_prompt_template = PromptTemplate.from_template("""
你扮演{person}
""")
example_template="""以下是一个互动示例：
Q:{example_q}
A:{example_a}
"""
example_prompt_template=PromptTemplate.from_template(example_template)

start_template="""以下是一个真实的互动:
Q:{input}
A:

"""
start_prompt_template = PromptTemplate.from_template(start_template)
from langchain_core.runnables import RunnablePassthrough

chain = (
    RunnablePassthrough.assign(
        introductx=lambda x: introduction_prompt_template.invoke({"person": x["person"]}),
        examplex=lambda x: example_prompt_template.invoke({"example_q": x["example_q"], "example_a": x["example_a"]}),
        startx=lambda x: start_prompt_template.invoke({"input": x["input"]})
    )
    | (lambda x: f"{x['introductx'].text}\n{x['examplex'].text}\n{x['startx'].text}")
    # 注意：这里使用单引号包裹键名，避免与外层双引号冲突
)

print(chain.invoke({"person":"ME","example_q":"1","example_a":"1","input":"1"}))
