from pipline.infra import *
from pipline.novel import NovelViewModel

from 

def generate_core(idea: str):
    """アイデアからコア要素の作成を行う"""
    for element in CORE_ELEMENTS.keys():
        _show_message("INFO", f"{element}の生成中...")
        core_element = _generate_core(idea, element)
        _show_message("INFO", f"{element}の生成完了")
        print(f"{element}:\n{core_element}\n")

def _generate_core(idea: str, element: str):
    """アイデアからコア要素を生成する関数"""
    # TODO: いずれ非同期化する
    return generate_core_elements(idea, element)

def _show_message(title: str, message: str):
    """メッセージを表示するための内部関数"""
    print(f"{title}: {message}")

def _check_by_user(message: str) -> bool:
    """ユーザーに確認を求める内部関数"""
    response = input(f"{message} (y/n): ")
    return response.lower() == 'y'
