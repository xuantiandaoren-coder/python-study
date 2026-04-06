import asyncio

from langchain_core.runnables import RunnableLambda

def add_one(x:int)->int:
    return x+1

async def add_two(x:int)->int:
    return x+2

runable_add_one = RunnableLambda(func=add_one,afunc=add_two)

print(runable_add_one.invoke(1))
print(runable_add_one.batch([1,2,3]))
async def main():
    print (await runable_add_one.ainvoke(2))

asyncio.run(main())