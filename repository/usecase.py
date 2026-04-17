from repository.files import FolderRepository, JsonRepository

PROMPT_FILENAMES = {
    "system": "system_prompt.txt",
    "user": "user_prompt.txt"
}

def setup():
    """初期設定。主にプロンプトの存在確認。"""
    for stage in ["base", "novel"]:
        dir = FolderRepository(folder_name=stage)
        for filename in PROMPT_FILENAMES.values():
            try:
                dir.get(filename)
            except FileNotFoundError as e:
                raise FileNotFoundError(f"Prompt file '{filename}' not found for stage '{stage}'. Please ensure it exists in the '{stage}' folder.") from e

def load_prompt(stage_folder: str, prompt_type: str) -> str:
    dir = FolderRepository(folder_name=stage_folder)
    return dir.get(PROMPT_FILENAMES[prompt_type]).read_text(encoding="utf-8")