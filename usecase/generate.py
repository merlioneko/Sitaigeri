from pipline.infra import *
from pipline.novel import NovelViewModel

def generate_novel(idea: str) -> tuple[str, str]:
    """与えられたアイデアからストーリープランと小説を生成する。"""
    novel_vm = NovelViewModel(idea=idea)
    try:
        novel_vm.idea = _generate_ideas(idea)
        novel_vm.plan = _generate_plan(novel_vm.idea)
        novel = _generate_novel(novel_vm.plan)
    except Exception as e:
        _show_message("ERROR", f"エラーが発生しました: {e}")
        novel_vm.plan = "ストーリープランの生成に失敗しました。"
        novel = "小説の生成に失敗しました。"
        
    return novel_vm.plan, novel

def _generate_ideas(idea: str) -> str:
    """ユーザーのアイデアをもとに新しいアイデアを生成する内部関数"""
    _show_message("INFO", "アイデア生成中...")
    while True:
        ideas = generate_developped_ideas(idea)
        _show_message("INFO", "アイデア生成完了")
        _show_message("INFO", "生成されたアイデア:")
        print(ideas)
        if _check_by_user("このアイデアでストーリープランを生成しますか？"):
            break
        else:
            _show_message("INFO", "アイデアを再生成します...")
    return ideas

def _generate_plan(idea: str) -> str:
    """アイデアからストーリープランを生成する内部関数"""
    _show_message("INFO", "ストーリープラン生成中...")
    while True:
        plan = generate_base_config(idea)
        _show_message("INFO", "ストーリープラン生成完了")
        _show_message("INFO", "生成されたストーリープラン:")
        print(plan)
        if _check_by_user("このストーリープランで小説を生成しますか？"):
            break
        else:
            _show_message("INFO", "ストーリープランを再生成します...")
    return plan

def _generate_novel(plan: str) -> str:
    """ストーリープランから小説を生成する内部関数"""
    _show_message("INFO", "小説本文生成中...")
    novel = generate_novel_text(plan)
    _show_message("INFO", "小説本文生成完了")
    return novel

def _show_message(title: str, message: str):
    """メッセージを表示するための内部関数"""
    print(f"{title}: {message}")

def _check_by_user(message: str) -> bool:
    """ユーザーに確認を求める内部関数"""
    response = input(f"{message} (y/n): ")
    return response.lower() == 'y'
