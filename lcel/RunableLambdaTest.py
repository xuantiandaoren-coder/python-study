from langchain_core.runnables import RunnableLambda

result = RunnableLambda(lambda x:x+1) | RunnableLambda(lambda x:x*2) | RunnableLambda(lambda x:print(x))
result.invoke(2)
