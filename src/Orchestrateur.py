from .api_key_manager import get_keys


from openai import OpenAI


class Orchestrateur:
    def __init__(self, model_name: str, provider_url: str) -> None:
        self.model_name = model_name
        self.provider_url = provider_url
        self.keys = get_keys()

    def call_api(self) -> str:
        with OpenAI(
            base_url= self.provider_url,
            api_key= self.keys[0]
        ) as client:
            responce = client.chat.completions.create(
                model=self.model_name,
            )