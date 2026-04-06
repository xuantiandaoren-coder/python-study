from langchain_core.runnables import RunnablePassthrough, RunnableLambda

passthrough=  RunnablePassthrough()

def add_extra(input_text):
    return {"name":input_text["name"],"extra":"附加信息"}


add_extra_runable = RunnableLambda(add_extra)
chain = passthrough|add_extra_runable
print(chain.invoke({"name":"张三","age":18}))

runable_1 = passthrough.assign(greet=lambda x:"hello")
print("---"*20)
chain = add_extra_runable|runable_1
print(chain.invoke({"name":"张三","age":18}))