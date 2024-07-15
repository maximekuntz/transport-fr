class Publisher:
    def __init__(self, name: str = None, type: str = None) -> None:
        self.name = name
        self.type = type

    @classmethod
    def from_dict(cls, data: dict):
        return Publisher(name=data["name"], type=data["type"])

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Publisher({self.name}, {self.type})"
