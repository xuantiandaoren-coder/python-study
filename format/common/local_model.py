from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


def local_model()->ChatOpenAI:
    load_dotenv()
    llm = ChatOpenAI(temperature=0,model="deepseek-chat")
    return llm