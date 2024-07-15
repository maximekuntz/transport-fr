class AOMResponse:
    """Autorité organisatrice des mobilités (AOM)"""

    def __init__(
        self,
        departement: str,
        forme_juridique: str,
        insee_commune_principale: str,
        nom: str,
        siren: str,
    ) -> None:
        self.departement = departement
        self.forme_juridique = forme_juridique
        self.insee_commune_principale = insee_commune_principale
        self.nom = nom
        self.siren = siren

    @classmethod
    def from_dict(cls, data: dict):
        return AOMResponse(
            departement=data["departement"],
            forme_juridique=data["forme_juridique"],
            insee_commune_principale=data["insee_commune_principale"],
            nom=data["nom"],
            siren=data["siren"],
        )

    def __str__(self) -> str:
        return self.nom

    def __repr__(self) -> str:
        s = (
            f"AOMResponse({self.departement}, {self.forme_juridique}, {self.insee_commune_principale}, "
            f"{self.nom}, {self.siren})"
        )
        return s


class AOMShortRef:
    """Autorité organisatrice des mobilités (AOM)
    DEPRECATED. Used for retrocompatibility only
    """

    def __init__(self, name: str, siren: str = None) -> None:
        self.name = name
        self.siren = siren

    @classmethod
    def from_dict(cls, data: dict):
        return AOMShortRef(**data)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"AOMShortRef({self.name}, {self.siren})"

    def __eq__(self, value: object) -> bool:
        return self.name == value.name and self.siren == value.siren
