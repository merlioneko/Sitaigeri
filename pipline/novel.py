class Novel:
    """生成中の小説モデルクラス"""
    def __init__(self, title: str = "",
                 theme: str = "",
                 idea: str = "",
                 plan: str = "",
                 setting: str = "",
                 tone: str = "",
                 characters: list[str] = [],
                 scenes: list[str] = []):
        self.title = title
        self.theme = theme
        self.idea = idea
        self.plan = plan
        self.setting = setting
        self.tone = tone
        self.characters = characters
        self.scenes = scenes

    def get_body(self) -> str:
        return "\n".join(self.scenes)
    
    def to_string(self) -> str:
        """小説の要素を文字列として返すためのメソッド"""
        elements = [
            f"Title: {self.title}",
            f"Theme: {self.theme}",
            f"Idea: {self.idea}",
            f"Plan: {self.plan}",
            f"Setting: {self.setting}",
            f"Tone: {self.tone}",
            f"Characters: {', '.join(self.characters)}",
            f"Scenes:\n{chr(10).join(self.scenes)}"
        ]
        return "\n".join(elements)

def set_element(novel: Novel, element_name: str, element_value):
    """小説の要素を設定するための関数"""
    if hasattr(novel, element_name):
        setattr(novel, element_name, element_value)
    else:
        raise AttributeError(f"Novel class has no attribute '{element_name}'")