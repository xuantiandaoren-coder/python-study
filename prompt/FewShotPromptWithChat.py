from langchain_core.prompts import PromptTemplate,FewShotChatMessagePromptTemplate,ChatPromptTemplate
from langchain_openai import ChatOpenAI
from common.local_model import local_model

model = local_model()

exapmles=[
    {"input":"北京天气怎么样","output":"北京市"},
    {"input":"南京是江苏的","output":"南京市"},
    {"input":"武汉有什么好吃的","output":"武汉市"}
     ]
    

example_prompt = ChatPromptTemplate([
    ("human","{input}"),
    ("ai","{output}")
    ])

few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples = exapmles,
    example_prompt = example_prompt,
   
)

# print(few_shot_prompt.invoke({}).to_string)

final_prompt_template = ChatPromptTemplate([
    ("system","你是个旅游家"),
    few_shot_prompt,
    ("human","{input}")
])

print(final_prompt_template.invoke({"input":"下扬州"}))
