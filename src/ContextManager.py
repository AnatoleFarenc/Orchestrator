from .Prompt import Prompt
from .config import (
    PATH_SYS_PROMPT, PATH_USER_PROMPT,
    SYS_VARIABLES, USER_VARIABLES
)

from openai.types.chat import ChatCompletionMessageParam
from typing import Optional, List


class ContextManager:
    def __init__(self, sys_promt_template_path: Optional[str] = None,
                 user_prompt_template_path: Optional[str] = None) -> None:
        sys_path = (sys_promt_template_path if sys_promt_template_path
                    else PATH_SYS_PROMPT)
        user_path = (user_prompt_template_path if user_prompt_template_path
                     else PATH_USER_PROMPT)
        self.__sys_prompt = Prompt(sys_path, SYS_VARIABLES)
        self.__user_prompt = Prompt(user_path, USER_VARIABLES)

    def build_context(
            self,
            user_prompt: str
    ) -> List[ChatCompletionMessageParam]:
        context = self.__content + self

    @property
    def sys_prompt(self) -> str:
        return self.__sys_prompt.prompt

    @sys_prompt.setter
    def sys_prompt(self, n_sys_prompt) -> None:
        self.__sys_prompt.prompt = n_sys_prompt

    @property
    def user_prompt(self) -> str:
        return self.__user_prompt.prompt

    @user_prompt.setter
    def user_prompt(self, n_user_prompt) -> None:
        self.__user_prompt.prompt = n_user_prompt
