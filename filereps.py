from pathlib import Path
import json

class FolderRepository:
    """指定された名前のフォルダをベースフォルダ(最基底ディレクトリ)基準で管理するリポジトリクラス。"""
    def __init__(self, folder_name: str):
        """指定された名前のフォルダをベースフォルダ基準で管理。存在しない場合には作成する"""
        self.base_folder = Path(__file__).resolve().parent.parent
        self.folder = self.base_folder / folder_name
        if not self.folder.exists():
            self.folder.mkdir(parents=True, exist_ok=True)

    def get(self, filename: str) -> Path:
        """フォルダ内の指定されたファイル/フォルダのPathを返す。存在しない場合にはFileNotFoundErrorを発生させる。"""
        file_path = self.folder / filename
        if not file_path.exists():
            raise FileNotFoundError(f"File or folder '{filename}' not found in folder '{self.folder}'")
        return file_path

class JsonRepository:
    def __init__(self, file_path: Path):
        """指定されたJSONファイルを管理。存在しない場合にはFileNotFoundErrorを発生させる。"""
        self.file_path = file_path
        if not self.file_path.exists():
            raise FileNotFoundError(f"JSON file '{file_path}' not found.")
    
    def read_json(self) -> dict:
        """JSONファイルを読み込んで辞書として返す。"""
        with self.file_path.open(encoding="utf-8") as f:
            return json.load(f)
    
    def write_json(self, data: dict):
        """辞書データをJSONファイルに書き込む。"""
        with self.file_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)