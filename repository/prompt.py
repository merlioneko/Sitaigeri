from abc import ABC, abstractmethod

class IJsonWrapper(ABC):
    @abstractmethod
    def to_json(self) -> dict:
        pass

class Prompt(IJsonWrapper):
    def __init__(self, role: str, content: str):
        self.role = role
        self.prompt = content

    def to_json(self) -> dict:
        return {
            "role": self.role,
            "content": self.prompt
        }

class SystemPrompt(Prompt):
    def __init__(self, prompt: str):
        super().__init__("system", prompt)

class UserPrompt(Prompt):
    def __init__(self, prompt: str):
        super().__init__("user", prompt)

class OutputJsonFormat:
    def __init__(self, schema: dict):
        self.format_type = "json_schema"
        self.schema = schema

    def to_json(self, name: str) -> dict:
        return {
            "type": self.format_type,
            "json_schema": {
                "name": name,
                "schema": self.schema
            }
        }