from transport_fr.objects.aom import AOMShortRef


class City:
    def __init__(self, insee: str, name: str) -> None:
        self.insee = insee
        self.name = name

    @classmethod
    def from_dict(cls, data: dict):
        return City(insee=data["insee"], name=data["name"])

    def __str__(self) -> str:
        return f"{self.name} ({self.insee})"

    def __repr__(self) -> str:
        return f"City({self.insee}, {self.name})"


class CoveredArea:
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    @classmethod
    def from_dict(cls, data: dict):
        if data["type"] == "cities":
            return Cities.from_dict(data)
        elif data["type"] == "region":
            return Region.from_dict(data)
        elif data["type"] == "country":
            return Country.from_dict(data)
        elif data["type"] == "aom":
            return AOM.from_dict(data)
        else:
            raise ValueError(f"Unknown type {data['type']}")


class Cities(CoveredArea):
    def __init__(self, cities: list[City], name: str, type: str) -> None:
        if type != "cities":
            raise ValueError(f"type should be 'cities'")
        CoveredArea.__init__(self, name=name, type=type)
        self.cities = cities

    @classmethod
    def from_dict(cls, data: dict):
        cities = [City.from_dict(city) for city in data["cities"]]
        return Cities(cities=cities, name=data["name"], type=data["type"])

    def __str__(self) -> str:
        return f"{self.name} ({self.cities})"

    def __repr__(self) -> str:
        return f"Cities({self.cities}, {self.name}, {self.type})"


class Region(CoveredArea):
    def __init__(self, region: str, name: str, type: str) -> None:
        if type != "region":
            raise ValueError(f"type should be 'region'")
        CoveredArea.__init__(self, name=name, type=type)
        self.region = region

    @classmethod
    def from_dict(cls, data: dict):
        return Region(region=data["region"], name=data["name"], type=data["type"])

    def __str__(self) -> str:
        return f"{self.name} ({self.region})"

    def __repr__(self) -> str:
        return f"Region({self.region}, {self.name}, {self.type})"


class Country(CoveredArea):
    def __init__(self, country: str, name: str, type: str) -> None:
        if type != "country":
            raise ValueError(f"type should be 'country'")
        CoveredArea.__init__(self, name=name, type=type)
        self.country = country

    @classmethod
    def from_dict(cls, data: dict):
        return Country(country=data["country"], name=data["name"], type=data["type"])

    def __str__(self) -> str:
        return f"{self.name} ({self.country})"

    def __repr__(self) -> str:
        return f"Country({self.country}, {self.name}, {self.type})"


class AOM(CoveredArea):
    """Autorité organisatrice des mobilités (AOM)"""

    def __init__(self, aom: AOMShortRef, name: str, type: str) -> None:
        if type != "aom":
            raise ValueError(f"type should be 'aom'")
        CoveredArea.__init__(self, name=name, type=type)
        self.aom = aom

    @classmethod
    def from_dict(cls, data: dict):
        return AOM(
            aom=AOMShortRef.from_dict(data["aom"]), name=data["name"], type=data["type"]
        )

    def __str__(self) -> str:
        return self.nom

    def __repr__(self) -> str:
        return f"AOM({self.aom}, {self.name}, {self.type})"
