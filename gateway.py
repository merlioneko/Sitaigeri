from openai import OpenAI
from abc import abstractmethod
from prompt import SystemPrompt, UserPrompt
from typing import Protocol

class ILlmPort(Protocol):
    @abstractmethod
    def response(self, system: (SystemPrompt| str), user: (UserPrompt|str)) -> str:
        pass

class LmStudioGateway(ILlmPort):
    def __init__(self, url: str, model_name: str):
        self.client = OpenAI(base_url=url, api_key="lm-studio")
        self.model_name = model_name

    def response(self, system: (SystemPrompt| str), user: (UserPrompt|str)) -> str:
        # Convert strings to Prompt objects if necessary
        if isinstance(system, str):
            system = SystemPrompt(system)
        if isinstance(user, str):
            user = UserPrompt(user)

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                system.to_json(),
                user.to_json()
            ]
        )
        content = response.choices[0].message.content
        return content
    
    def response_with_format(self, system: (SystemPrompt| str), user: (UserPrompt|str), response_format: dict) -> str:
        # Convert strings to Prompt objects if necessary
        if isinstance(system, str):
            system = SystemPrompt(system)
        if isinstance(user, str):
            user = UserPrompt(user)

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                system.to_json(),
                user.to_json()
            ],
            response_format=response_format
        )
        content = response.choices[0].message.content
        return content