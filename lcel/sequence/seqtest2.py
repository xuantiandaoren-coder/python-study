from typing import Any

from langchain_core.runnables import Runnable


class DataValidator(Runnable):
    def invoke(self,input:dict[str,Any],config:Any=None,**kwargs)->dict[str,Any]:
        if "name" not in input or "age" not in input:
            raise ValueError("Missing 'name' and 'age' in input")
        return input

class AgeTransformer(Runnable):
    def invoke(self,input:dict[str,Any],config:Any=None)->dict[str,Any]:
        return {
            **input,
            "age_group":"yong" if input["age"]<35 else "中年"
        }

pipline = DataValidator()|AgeTransformer()
print(pipline.get_graph().draw_ascii())

print(pipline.invoke({"name":"alis","age":29}))