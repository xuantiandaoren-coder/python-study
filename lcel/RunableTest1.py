from typing import Iterator, AsyncIterator

from langchain_core.runnables import Runnable
from langchain_core.runnables.utils import Output


class TextTranfromer(Runnable):

    def __init__(self, prefix:str = "处理后的文本") -> None:
        self.prefix = prefix

    def invoke(self, input: str) -> str:
        processed_text = input.upper()
        return f"{self.prefix}{processed_text}"
    async def invoke_async(self, input: str) -> str:
        return self.invoke(input)

    def stream(self, input: str) -> Iterator[str]:
        processed_text = input.upper()
        for char in processed_text:
            yield f"{self.prefix}{char}"

    async def astream(self, input: str) -> AsyncIterator[str]:
        return self.stream(input)

    def batch(self, input:list [str]) -> list[str]:
        return [self.invoke(input) for input in input]

    async def abatch(self,inputs:list[str]) -> list[Output]:
        return [await self.ainvoke(input) for input in inputs]


tranfromer = TextTranfromer()
result = tranfromer.invoke("hello world")
print(result)

for chunk in tranfromer.stream("hello world"):
    print(chunk)

