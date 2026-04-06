from logging.handlers import RotatingFileHandler
from tokenize import generate_tokens
from typing import Optional

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from common.local_model import local_model

llm = local_model()

class Movie(BaseModel):
    title:str = Field(description="电影标题")
    director:str = Field(description="导演姓名")
    year:int = Field(description="上映年份",ge=1900,le=2023)
    genres:list[str]=Field(description="电影类型列表")
    rating:Optional[float] = Field(description="电影评分0-10之间",ge=0,le=10)

template= """
你是一个电影信息提取助手，请从以下文本中提取电影信息，并以json格式返回。
文本:{text}
{format_instructions}
"""

paraser = PydanticOutputParser(pydantic_object=Movie)

prompt_template = PromptTemplate(
    template=template,
    input_variables=["text"],
    partial_variables={"format_instructions":paraser.get_format_instructions()}
)

movie_text="""
坦尼克号是一部由詹姆斯.卡梅隆执导的史诗级浪漫灾难电影
这部电影于1997年上映，讲述了穷画家杰克和贵族女露丝的爱情故事
他被归类为爱情、灾年和剧情片，获得了评论界和观众的广泛好评，IMD评分8.8分
"""

final_prompt = prompt_template.format(text=movie_text)

print(final_prompt)

resp = llm.invoke(final_prompt)

print(paraser.invoke(resp))
