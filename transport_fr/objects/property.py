class Property:
    def __init__(self, id: str | int) -> None:
        self.id = id

    @staticmethod
    def from_dict(data: dict):
        return Property(id=data["id"])

    def __str__(self) -> str:
        return f"Property {self.id}"

    def __repr__(self) -> str:
        return f"Property(id={self.id})"
