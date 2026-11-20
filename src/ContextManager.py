from .Prompt import Prompt


from typing import Optional


class ContextManager:
    def __init__(self, promt_template_path: Optional[str] = None) -> None:
        self.__context = Prompt(promt_template_path)

    @property
    def context(self) -> str:
        return self.__context.prompt

    @context.setter
    def context(self, new_context: str) -> None:
        self.__context.prompt = new_context
