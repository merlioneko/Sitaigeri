from abc import ABC, abstractmethod

class IJsonWrapper(ABC):
    @abstractmethod
    def to_json(self) -> dict:
        pass

class Prompt(IJsonWrapper):
    def __init__(self, role: str, prompt: str):
        self.role = role
        self.prompt = prompt

    def to_json(self) -> dict:
        return {
            "role": self.role,
            "prompt": self.prompt
        }

class SystemPrompt(Prompt):
    def __init__(self, prompt: str):
        super().__init__("system", prompt)

class UserPrompt(Prompt):
    def __init__(self, prompt: str):
        super().__init__("user", prompt)