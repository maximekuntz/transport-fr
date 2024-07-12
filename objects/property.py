class Property:
    def __init__(self, id: str | int) -> None:
        self.id = id

    def __str__(self) -> str:
        return f"Property {self.id}"
