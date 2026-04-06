from langchain_core.runnables import RunnableLambda, RunnableSequence


def add_one(input: str) -> str:
    return input + " 1"

def mul_two(input: str) -> str:
    return input * 2

add_one_runable = RunnableLambda(add_one)
add_two_runable = RunnableLambda(mul_two)

seq = RunnableSequence(add_one_runable, add_two_runable)
# seq = add_one_runable | add_two_runable

print(seq.get_graph().draw_ascii())