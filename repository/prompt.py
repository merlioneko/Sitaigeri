from abc import ABC, abstractmethod

class IJsonWrapper(ABC):
    @abstractmethod
    def to_json(self) -> dict:
        pass

class Prompt(IJsonWrapper):
    def __init__(self, role: str, contents: str):
        self.role = role
        self.contents = contents

    def to_json(self) -> dict[str, str]:
        return {
            "role": self.role,
            "contents": self.contents
        }

class SystemPrompt(Prompt):
    def __init__(self, contents: str):
        super().__init__("system", contents)

class UserPrompt(Prompt):
    def __init__(self, contents: str):
        super().__init__("user", contents)

class OutputJsonFormat:
    def __init__(self, schema: dict):
        self.format_type = "json_schema"
        self.schema = schema

    def to_json(self, name: str) -> dict[str, object]:
        return {
            "type": self.format_type,
            "json_schema": {
                "name": name,
                "schema": self.schema
            }
        }