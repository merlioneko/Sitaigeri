from filereps import FolderRepository, JsonRepository

PROMPT_FILENAMES = {
    "system": "system_prompt.txt",
    "user": "user_prompt.txt"
}

PROMPT_DIRNAMES = ["develop", "base", "novel"]

def setup():
    """初期設定。主にプロンプトの存在確認。"""
    for stage in PROMPT_DIRNAMES:
        dir = FolderRepository(folder_name=stage)
        for filename in PROMPT_FILENAMES.values():
            if not dir.get(filename).exists():
                dir.get(filename).open("w", encoding="utf-8").close()  # 空のファイルを作成

def load_prompt(stage_folder: str, prompt_type: str) -> str:
    dir = FolderRepository(folder_name=stage_folder)
    return dir.get(PROMPT_FILENAMES[prompt_type]).read_text(encoding="utf-8")