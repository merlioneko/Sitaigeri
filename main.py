from usecase.generate import generate_novel
from ui import *

from repository.files import FolderRepository

def get_idea() -> str:
    """idea/idea.txtからアイデアを読み込む"""
    try:
        idea_file = FolderRepository(folder_name="idea").get("idea.txt")
        return idea_file.read_text(encoding="utf-8")
    except FileNotFoundError as e:
        raise FileNotFoundError("Idea file not found. Please ensure 'idea/idea.txt' exists.") from e

def generate_and_display(idea: str):
    """LLMで小説を生成してGUIに表示"""
    plan, novel = generate_novel(idea)
    display_novel_gui(plan, novel)

if __name__ == "__main__":
    try:
        idea = get_idea()
        generate_and_display(idea)
    except FileNotFoundError as e:
        display_message(title="エラー", message=e.args[0])
