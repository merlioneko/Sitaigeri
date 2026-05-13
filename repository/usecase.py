from pathlib import Path
import sys

# 親ディレクトリをPythonパスに追加
sys.path.insert(0, str(Path(__file__).resolve().parent))

from filereps import FolderRepository, JsonRepository
from json_structure.core_elements import CORE_ELEMENTS

PROMPT_FILENAMES = {
    "system": "system_prompt.txt",
    "user": "user_prompt.txt"
}

USER_ELEMENTS = ["idea"]
PROMPT_DIRNAMES = USER_ELEMENTS + list(CORE_ELEMENTS.keys())

PROMPTS_DIR = "prompts/"

def setup():
    """初期設定。主にプロンプトの存在確認。"""
    for stage in PROMPT_DIRNAMES:
        dir = FolderRepository(folder_name=PROMPTS_DIR + stage)
        for filename in PROMPT_FILENAMES.values():
            if not dir.get(filename).exists():
                dir.get(filename).open("w", encoding="utf-8").close()  # 空のファイルを作成

def load_prompt(stage_folder: str, prompt_type: str) -> str:
    dir = FolderRepository(folder_name=PROMPTS_DIR + stage_folder)
    return dir.get(PROMPT_FILENAMES[prompt_type]).read_text(encoding="utf-8")