from langchain_core.runnables import RunnableLambda, RunnableParallel


def add_one(num):
    return num + 1
def mul_two(num):
    return num * 2
def mul_three(num):
    return num * 3

def add_two(input:dict)->int:
    return input["mul_two"]+input["mul_three"]

runable_1 = RunnableLambda(add_one)
runable_2 = RunnableLambda(mul_two)
runable_3 = RunnableLambda(mul_three)
runable_4 = RunnableLambda(add_two)

# pipleline = runable_1 | RunnableParallel(
#     {"mul_two":runable_2,
#     "mul_three":runable_3}
# )
# print(pipleline.get_graph().draw_ascii())
# print(pipleline.invoke(1))

pipleline = runable_1 | {"mul_two":runable_2,
    "mul_three":runable_3}|runable_4

print(pipleline.get_graph().draw_ascii())
print(pipleline.invoke(1))