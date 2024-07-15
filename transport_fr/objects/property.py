class Property:
    def __init__(self, id: str | int) -> None:
        self.id = id

    @classmethod
    def from_dict(cls, data: dict):
        return Property(id=data["id"])

    def __str__(self) -> str:
        return f"Property {self.id}"
