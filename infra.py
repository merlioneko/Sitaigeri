from pathlib import Path
from openai import OpenAI
import json

from output_structure import base_json

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
model_name = "berghof-nsfw-7b-i1@q6_k_s"

PROMPT_FILENAMES = {
    "system": ["system_pronpt.txt", "system_prompt.txt"],
    "user": ["user_pronpt.txt", "user_prompt.txt"]
}


def load_prompt(stage_folder: str, prompt_type: str) -> str:
    base_dir = Path(__file__).resolve().parent
    folder = base_dir / stage_folder
    for filename in PROMPT_FILENAMES[prompt_type]:
        prompt_path = folder / filename
        if prompt_path.exists():
            return prompt_path.read_text(encoding="utf-8")

    checked = ", ".join(str(folder / name) for name in PROMPT_FILENAMES[prompt_type])
    raise FileNotFoundError(
        f"Prompt file not found for {prompt_type} in {stage_folder}. Checked: {checked}"
    )


def generate_base_config(raw_idea: str) -> str:
    # ネタ → キャラクター・ストーリーライン
    system_prompt = load_prompt("base", "system")
    user_prompt = load_prompt("base", "user")
    output_structure_json = base_json

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"{user_prompt}\n{raw_idea}"}
        ],
        response_format={
            "type": "json_schema",
            "json_schema": { 
                "name": "story_schema",
                "schema": output_structure_json
            }
        }
    )
    content = response.choices[0].message.content
    return (
        content
        if isinstance(content, str)
        else json.dumps(content, ensure_ascii=False, indent=2)
    )


def generate_novel_text(story_plan: str) -> str:
    # ストーリーライン → 小説本文
    system_prompt = load_prompt("novel", "system")
    user_prompt = load_prompt("novel", "user")
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"{user_prompt}\n{story_plan}"}
        ]
    )
    return response.choices[0].message.content
