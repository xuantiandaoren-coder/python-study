from langchain_core.prompts import PromptTemplate
from datetime import datetime
#group1
prompt_template = PromptTemplate.from_template("calc 1+1+2 need three step,first:{first},second:{second},third{third}")
first_prompt_template = prompt_template.partial(first="1+1")
second_prompt_template = first_prompt_template.partial(second="2+1")
final_prompt = second_prompt_template.invoke({"third":"3=3"})
print(final_prompt)

#group2
prompt_template = PromptTemplate(template="calc 1+1+2 need three step,first:{first},second:{second},third{third}",
                                               input_variables=["second","third"],
                                               partial_variables={"first":"1+1"}
                                               )
second_prompt_template = first_prompt_template.partial(second="2+1")
final_prompt = second_prompt_template.invoke({"third":"3=3"})
print(final_prompt)

#group3
def _get_datetime():
    now = datetime.now()
    return now.strftime("%Y/%m/%d")

prompt_template = PromptTemplate(template="tell me what happen:{date}，about{who}",input_variables=["who","date"])
partial_prompt_template1 = prompt_template.partial(date=_get_datetime)
partial_prompt_template2 = prompt_template.partial(date="2025/04/04")

print(partial_prompt_template1.invoke({"who":"me"}))
print(partial_prompt_template2.invoke({"who":"you"}))



