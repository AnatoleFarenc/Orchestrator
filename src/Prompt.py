from .config import PATH_PROMPT

from typing import Optional
from string import Template


class Prompt:
    def __init__(self, prompt_path: Optional[str] = None) -> None:
        p_path = prompt_path if prompt_path else PATH_PROMPT
        with open(p_path, 'r') as f:
            self._prompt_template = f.read()
        self._prompt = self._build_prompt_with_template()

    def _render_prompt(self, **value: object) -> str:
        template = Template(self._prompt_template)
        return template.substitute(value).strip()

    def _build_prompt_with_template(self) -> str:
        return self._render_prompt(
            tools_manual="No tools"
        )

    @property
    def prompt(self) -> str:
        return self._prompt

    @prompt.setter
    def prompt(self, prompt: str) -> None:
        self._prompt = prompt
