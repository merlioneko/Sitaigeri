from infra import *

def generate_novel(idea: str) -> tuple[str, str]:
    """与えられたアイデアからストーリープランと小説を生成する。"""
    try:
        print("ストーリープラン生成中...")
        plan = generate_base_config(idea)
        print("ストーリープラン生成完了")
        print("小説本文生成中...")
        novel = generate_novel_text(plan)
        print("小説本文生成完了")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        plan = "ストーリープランの生成に失敗しました。"
        novel = "小説の生成に失敗しました。"
    return plan, novel
