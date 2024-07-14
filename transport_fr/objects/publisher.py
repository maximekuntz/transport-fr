class Publisher:
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Publisher(name={self.name}, type={self.type})"
