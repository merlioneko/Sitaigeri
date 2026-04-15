from abc import ABC, abstractmethod

class IJsonWrapper(ABC):
    @abstractmethod
    def to_json(self) -> dict:
        pass

class Prompt(IJsonWrapper):
    def __init__(self, roll: str, prompt: str):
        self.roll = roll
        self.prompt = prompt

    def to_json(self) -> dict:
        return {
            "roll": self.roll,
            "prompt": self.prompt
        }

class SystemPrompt(Prompt):
    def __init__(self, prompt: str):
        super().__init__("system", prompt)

class UserPrompt(Prompt):
    def __init__(self, prompt: str):
        super().__init__("user", prompt)