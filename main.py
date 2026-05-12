from usecase.generate import *
from repository.usecase import setup
from ui import *

from filereps import FolderRepository

def get_idea() -> str:
    """idea/idea.txtからアイデアを読み込む"""
    try:
        idea_file = FolderRepository(folder_name="idea").get("idea.txt")
        return idea_file.read_text(encoding="utf-8")
    except FileNotFoundError as e:
        return e.__str__()


if __name__ == "__main__":
    setup()  # プロンプトの存在確認と空ファイルの作成
    try:
        idea = get_idea()
        print(idea)
    except FileNotFoundError as e:
        display_message(title="エラー", message=e.__str__())
