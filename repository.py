from pathlib import Path
import json

class FolderRepository:
    def __init__(self, folder_name: str):
        """指定された名前のフォルダをベースフォルダ基準で管理。存在しない場合には例外を発生させる。"""
        self.base_folder = Path(__file__).resolve().parent
        self.folder = self.base_folder / folder_name
        if not self.folder.exists():
            raise FileNotFoundError(f"Folder '{folder_name}' not found in {self.base_folder}")

class JsonRepository:
    def __init__(self, file_path: Path):
        """指定されたJSONファイルを管理。存在しない場合には例外を発生させる。"""
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