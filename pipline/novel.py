class NovelViewModel:
    """生成中の小説モデルクラス"""
    def __init__(self, title: str = "",
                 idea: str = "",
                 plan: str = "",
                 characters: list[str] = [],
                 scenes: list[str] = []):
        self.title = title
        self.idea = idea
        self.plan = plan
        self.characters = characters
        self.scenes = scenes

    def get_body(self) -> str:
        return "\n".join(self.scenes)