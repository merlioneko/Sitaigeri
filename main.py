from domain import generate_novel
from ui import *
from pathlib import Path

NO_DATA_MESSAGE = "idea/idea.txt が見つかりません。アイデアを idea/idea.txt に保存してください。" 

idea_dir = Path(__file__).resolve().parent / "idea"
idea_file = idea_dir / "idea.txt"
idea = idea_file.read_text(encoding="utf-8") if idea_file.exists() else NO_DATA_MESSAGE

def generate_and_display():
    #LLMで小説を生成してGUIに表示
    if idea == NO_DATA_MESSAGE:
        display_message("アイデアが見つかりませんでした。", "idea/idea.txt にアイデアを保存してください。")
        return
    plan, novel = generate_novel(idea)
    display_novel_gui(plan, novel)


if __name__ == "__main__":
    generate_and_display()
