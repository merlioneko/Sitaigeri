from pathlib import Path
import json
from filereps import JsonRepository

from gateway.gateway import OpenAiGateway, TestGateway
from repository.usecase import load_prompt
from json_structure.core_elements import *


server_url = "http://localhost:1234/v1"
model_name = JsonRepository(file_path=Path(__file__).parent.parent / "model_name.json").read_json()["model_name"]

llm_port = TestGateway(url=server_url, model_name=model_name)

def generate_core_elements(idea: str, element: str) -> str:
    """アイデアからコア要素を生成する関数"""
    system_prompt = load_prompt("core_elements", "system")
    user_prompt = load_prompt("core_elements", "user").replace("{element}", element)
    response = llm_port.response(
        system=system_prompt,
        user=f"{user_prompt}\n{idea}",
        output_format=CORE_ELEMENTS.get(element)
    )
    return (
        response if isinstance(response, str)
        else json.dumps(response, ensure_ascii=False, indent=2)
    )

def generate_developped_ideas(idea: str) -> str:
    """ユーザーのアイデアをもとに新しいアイデアを生成する"""
    system_prompt = load_prompt("develop", "system")
    user_prompt = load_prompt("develop", "user")
    response = llm_port.response(
        system=system_prompt,
        user=f"{user_prompt}\n{idea}"
    )
    return response if response else ""


def generate_novel_text(story_plan: str) -> str:
    """ストーリーライン → 小説本文"""
    system_prompt = load_prompt("novel", "system")
    user_prompt = load_prompt("novel", "user")
    response = llm_port.response(
        system=system_prompt,
        user=f"{user_prompt}\n{story_plan}"
    )
    return response if response else ""
