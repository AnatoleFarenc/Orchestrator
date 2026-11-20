from .api_key_manager import get_keys
from .ContextManager import ContextManager
from .config import STOP_PROMPT


from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from typing import Optional, List


class Orchestrateur:
    def __init__(self, model_name: str, provider_url: str,
                 sys_prompt_template_path: Optional[str] = None) -> None:
        self.model_name = model_name
        self.provider_url = provider_url
        self.keys = get_keys()
        self.context_manager = ContextManager(sys_prompt_template_path)
        self.context: List[ChatCompletionMessageParam] = []

    def call_api(self) -> str:
        with OpenAI(
            base_url=self.provider_url,
            api_key=self.keys[0]
        ) as client:
            responce = client.chat.completions.create(
                model=self.model_name,
                messages=self.context,
                stop=STOP_PROMPT,
            )