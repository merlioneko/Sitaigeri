from pathlib import Path
import json
from repository.files import FolderRepository, JsonRepository

from gateway.gateway import LmStudioGateway
from repository.files import FolderRepository
from json_structure.novel_per_scene import base_json

server_url = "http://localhost:1234/v1"
model_name = JsonRepository(file_path=Path(__file__).parent / "model_name.json").read_json()["model_name"]

llm_port = LmStudioGateway(url=server_url, model_name=model_name)

PROMPT_FILENAMES = {
    "system": "system_prompt.txt",
    "user": "user_prompt.txt"
}

def setup():
    """初期設定。主にプロンプトの存在確認。"""
    for stage in ["base", "novel"]:
        dir = FolderRepository(folder_name=stage)
        for prompt_type, filename in PROMPT_FILENAMES.items():
            try:
                dir.get(filename)
            except FileNotFoundError as e:
                raise FileNotFoundError(f"Prompt file '{filename}' not found for stage '{stage}'. Please ensure it exists in the '{stage}' folder.") from e

def load_prompt(stage_folder: str, prompt_type: str) -> str:
    dir = FolderRepository(folder_name=stage_folder)
    return dir.get(PROMPT_FILENAMES[prompt_type]).read_text(encoding="utf-8")



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
    # ストーリーライン → 小説本文
    system_prompt = load_prompt("novel", "system")
    user_prompt = load_prompt("novel", "user")
    response = llm_port.response(
        system=system_prompt,
        user=f"{user_prompt}\n{story_plan}"
    )
    return response
