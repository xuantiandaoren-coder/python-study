from logging.handlers import RotatingFileHandler
from tokenize import generate_tokens
from typing import Optional

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_classic.output_parsers import OutputFixingParser
from common.local_model import local_model

llm = local_model()

class Movie(BaseModel):
    title:str = Field(description="电影标题")
    director:str = Field(description="导演姓名")
    year:int = Field(description="上映年份",ge=1900,le=2023)

parser = PydanticOutputParser(pydantic_object=Movie)
bad_output='{"title":"卧虎藏龙","director":"李安"}'
try:
    parser.parse(bad_output)
except Exception as e:
    print("错误:",e)

fix_parser = OutputFixingParser.from_llm(parser=parser,llm=llm)
print(fix_parser.invoke(bad_output))