from pathlib import Path
from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
model_name = "berghof-nsfw-7b-i1@q4_k_s"

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
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"{user_prompt}\n{raw_idea}"}
        ]
    )
    return response.choices[0].message.content


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


def generate_novel(idea: str) -> tuple[str, str]:
    """与えられたアイデアからストーリープランと小説を生成する。"""
    plan = generate_base_config(idea)
    print("ストーリープラン生成完了")
    novel = generate_novel_text(plan)
    print("小説本文生成完了")
    return plan, novel
