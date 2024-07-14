class City:
    def __init__(self, insee: str, name: str) -> None:
        self.insee = insee
        self.name = name

    def __str__(self) -> str:
        return f"{self.name} ({self.insee})"

    def __repr__(self) -> str:
        return f"City({self.insee}, {self.name})"


class CoveredArea:
    pass


class Cities(CoveredArea):
    def __init__(self, cities: list[City], name: str, type: str) -> None:
        CoveredArea.__init__(self)
        self.cities = cities
        self.name = name
        self.type = type

    def __str__(self) -> str:
        return f"{self.name} ({self.cities})"

    def __repr__(self) -> str:
        return f"Cities({self.cities}, {self.name}, {self.type})"


class Region(CoveredArea):
    def __init__(self, region_name: str, name: str, type: str) -> None:
        CoveredArea.__init__(self)
        self.region_name = region_name
        self.name = name
        if type != "region":
            raise ValueError(f"type should be 'region'")
        self.type = type

    def __str__(self) -> str:
        return f"{self.name} ({self.region_name})"

    def __repr__(self) -> str:
        return f"Region({self.region_name}, {self.name}, {self.type})"


class Country(CoveredArea):
    def __init__(self, country_name: str, name: str, type: str) -> None:
        CoveredArea.__init__(self)
        self.country_name = country_name
        self.name = name
        if type != "country":
            raise ValueError(f"type should be 'country'")
        self.type = type

    def __str__(self) -> str:
        return f"{self.name} ({self.country_name})"

    def __repr__(self) -> str:
        return f"Country({self.country_name}, {self.name}, {self.type})"


class AOM(CoveredArea):
    """Autorité organisatrice des mobilités (AOM)"""

    def __init__(
        self,
        departement: str,
        forme_juridique: str,
        insee_commune_principale: str,
        nom: str,
        siren: str,
    ) -> None:
        CoveredArea.__init__(self)
        self.departement = departement
        self.forme_juridique = forme_juridique
        self.insee_commune_principale = insee_commune_principale
        self.nom = nom
        self.siren = siren

    def __str__(self) -> str:
        return self.nom

    def __repr__(self) -> str:
        s = (
            f"AOM({self.departement}, {self.forme_juridique}, {self.insee_commune_principale}, "
            f"{self.nom}, {self.siren})"
        )
        return s

    def __eq__(self, value: object) -> bool:
        return self.nom == value.nom and self.siren == value.siren
