from main_logic import generate_novel
from ui import display_novel_gui

idea = "孤独なAIが人間の感情を学ぶSF"


def generate_and_display():
    #LLMで小説を生成してGUIに表示
    plan, novel = generate_novel(idea)
    display_novel_gui(plan, novel)


if __name__ == "__main__":
    generate_and_display()
