from pathlib import Path
import json
from filereps import JsonRepository

from gateway.gateway import LmStudioGateway, TestGateway
from repository.usecase import load_prompt
from json_structure.novel_per_scene import base_json


server_url = "http://localhost:1234/v1"
model_name = JsonRepository(file_path=Path(__file__).parent.parent / "model_name.json").read_json()["model_name"]

llm_port = TestGateway(url=server_url, model_name=model_name)


def generate_base_config(raw_idea: str) -> str:
    """ネタ → キャラクター・ストーリーライン"""
    system_prompt = load_prompt("base", "system")
    user_prompt = load_prompt("base", "user")
    output_structure_json = base_json

    response = llm_port.response(
        system=system_prompt,
        user=f"{user_prompt}\n{raw_idea}",
        output_format={
            "type": "json_schema",
            "json_schema": { 
                "name": "story_schema",
                "schema": output_structure_json
            }
        }
    )
    return (
        response if isinstance(response, str)
        else json.dumps(response, ensure_ascii=False, indent=2)
    )


def generate_novel_text(story_plan: str) -> str:
    """ストーリーライン → 小説本文"""
    system_prompt = load_prompt("novel", "system")
    user_prompt = load_prompt("novel", "user")
    response = llm_port.response(
        system=system_prompt,
        user=f"{user_prompt}\n{story_plan}"
    )
    return response
