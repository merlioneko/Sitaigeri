from openai import OpenAI
from abc import abstractmethod
from repository.prompt import SystemPrompt, UserPrompt
from typing import Protocol

class ILlmPort(Protocol):
    @abstractmethod
    def response(self,
                 system: (SystemPrompt| str),
                 user: (UserPrompt|str),
                 output_format: (dict|None) = None) -> str|None:
        pass

class OpenAiGateway(ILlmPort):
    def __init__(self, url: str, model_name: str):
        self.client = OpenAI(base_url=url, api_key="lm-studio")
        self.model_name = model_name

    def response(self,
                  system: (SystemPrompt|str),
                  user: (UserPrompt|str),
                  output_format: (dict|None) = None) -> str|None:
        # Convert strings to Prompt objects if necessary
        if isinstance(system, str):
            system = SystemPrompt(system)
        if isinstance(user, str):
            user = UserPrompt(user)

        message = [
            {"role": system.role, "content": system.prompt},
            {"role": user.role, "content": user.prompt}
        ]
        
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=message # type: ignore
        )

        content = response.choices[0].message.content
        return content

class TestGateway(ILlmPort):
    def __init__(self, url: str, model_name: str):
        self.url = url
        self.model_name = model_name
    def response(self, system: (SystemPrompt| str), user: (UserPrompt|str), output_format: (dict|None) = None) -> str|None:
        return "これはテスト用のダミー応答です。"