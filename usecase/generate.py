from pipline.infra import *
from pipline.novel import Novel, set_element

def generate_core(idea: str) -> Novel:
    """アイデアからコア要素の作成を行い、Novelオブジェクトを返す関数"""
    novel = Novel()
    for element in CORE_ELEMENTS.keys():
        _show_message("INFO", f"{element}の生成中...")
        core_element = _generate_core(idea, element, novel)
        set_element(novel, element, core_element)

        _show_message("INFO", f"{element}の生成完了")
        print(f"{element}:\n{core_element}\n")
    return novel

def _generate_core(idea: str, element: str, novel: Novel|None=None):
    """アイデアからコア要素を生成する関数"""
    # TODO: いずれ非同期化する
    novel_info = f"\n{element}:\n{novel.to_string()}" if novel else ""
    return generate_core_elements(idea+novel_info, element)

def _show_message(title: str, message: str):
    """メッセージを表示するための内部関数"""
    print(f"{title}: {message}")

def _check_by_user(message: str) -> bool:
    """ユーザーに確認を求める内部関数"""
    response = input(f"{message} (y/n): ")
    return response.lower() == 'y'
