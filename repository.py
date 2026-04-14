from pathlib import Path

class FolderRepository:
    def __init__(self, folder_name: str):
        """指定された名前のフォルダをベースフォルダ基準で管理。存在しない場合には例外を発生させる。"""
        self.base_folder = Path(__file__).resolve().parent
        self.folder = self.base_folder / folder_name
        if not self.folder.exists():
            raise FileNotFoundError(f"Folder '{folder_name}' not found in {self.base_folder}")