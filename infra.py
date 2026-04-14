from pathlib import Path
from openai import OpenAI
import json

from gateway import LmStudioGateway
from repository import FolderRepository
from output_structure import base_json

server_url = "http://localhost:1234/v1"
model_name = "berghof-nsfw-7b-i1@q6_k_s"

llm_port = LmStudioGateway(url=server_url, model_name=model_name)

PROMPT_FILENAMES = {
    "system": ["system_pronpt.txt", "system_prompt.txt"],
    "user": ["user_pronpt.txt", "user_prompt.txt"]
}

base_dir = FolderRepository(folder_name="base")
novel_dir = FolderRepository(folder_name="novel")


def load_prompt(stage_folder: str, prompt_type: str) -> str:
    dirs = [base_dir, novel_dir]
    for filename in PROMPT_FILENAMES[prompt_type]:
        for folder in dirs:
            prompt_path = folder.folder / filename
            if prompt_path.exists():
                return prompt_path.read_text(encoding="utf-8")

    checked = ", ".join(str(base_dir.base_folder / name) for name in PROMPT_FILENAMES[prompt_type])
    raise FileNotFoundError(
        f"Prompt file not found for {prompt_type} in {stage_folder}. Checked: {checked}"
    )


def generate_base_config(raw_idea: str) -> str:
    # ネタ → キャラクター・ストーリーライン
    system_prompt = load_prompt("base", "system")
    user_prompt = load_prompt("base", "user")
    output_structure_json = base_json

    response = llm_port.response_with_format(
        system=system_prompt,
        user=f"{user_prompt}\n{raw_idea}",
        response_format={
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
