from typing import Any,Dict,List

from langchain_core.example_selectors import BaseExampleSelector
class CustomerSelector(BaseExampleSelector):
    def __init__(self,examples:List[dict[str,any]]):
        self.examples = examples

    """custom example selector"""
    def add_example(self, example:dict[str,Any])->Any:
        self.examples.append(example)
    
    def select_examples(self, input_variables:dict[str,Any])->list[dict[str,str]]:
        disease_name = input_variables.get("disease_name",None)
        if disease_name is None:
            return []
        selected_examples = [
            example for example in self.examples
            if disease_name.lower() in example["input"].lower()
        ]
        return selected_examples


    