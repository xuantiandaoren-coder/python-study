import time
from random import random

from langchain_core.runnables import Runnable, RunnableLambda


def add_one(x):
    return x + 1

def double(x):
    start_time = time.time()
    format_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(format_time)
    r = random(x)
    if r < 0.1:
        print("happen exception")
        raise ValueError(f"happen exception,r{r}")
    return x * 2

pipline = RunnableLambda(add_one)|RunnableLambda(double).with_retry(stop_after_attempt=5)

print(pipline.invoke(0.1))


