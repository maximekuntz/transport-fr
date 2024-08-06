class Publisher:
    def __init__(self, name: str = None, type: str = None) -> None:
        self.name = name
        self.type = type

    @staticmethod
    def from_dict(data: dict):
        return Publisher(name=data["name"], type=data["type"])

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Publisher(name={self.name}, type={self.type})"
