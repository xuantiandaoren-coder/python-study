import asyncio

from langchain_core.runnables import RunnableLambda

def multiply(a,b):
    return a*b

def multiply_dic_wrapper(inputs:dict):
    return multiply(**inputs)

runable_lambda = RunnableLambda(multiply_dic_wrapper)
print(runable_lambda.invoke({'a':1,'b':2}))

def multiply_tuple_wrapper(inputs:tuple):
    return multiply(*inputs)
runable_lambda = RunnableLambda(multiply_tuple_wrapper)
print(runable_lambda.invoke((3,3)))

class MultiplyParametrized(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

def multiply_parmaters_wrapper(inputs:MultiplyParametrized):
    return multiply(inputs.a,inputs.b)
runable_lambda = RunnableLambda(multiply_parmaters_wrapper)
print(runable_lambda.invoke(MultiplyParametrized(3,3)))