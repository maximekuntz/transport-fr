class Place:
    def __init__(self, name: str, type: str, url: str) -> None:
        self.name = name
        self.type = type
        self.url = url

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Place(name={self.name}, type={self.type}, url={self.url})"
