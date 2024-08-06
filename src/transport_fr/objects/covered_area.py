from transport_fr.objects.aom import AOMShortRef


class City:
    def __init__(self, insee: str, name: str) -> None:
        self.insee = insee
        self.name = name

    @staticmethod
    def from_dict(data: dict):
        return City(insee=data["insee"], name=data["name"])

    def __str__(self) -> str:
        return f"{self.name} ({self.insee})"

    def __repr__(self) -> str:
        return f"City(insee={self.insee}, name={self.name})"


class CoveredArea:
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    @staticmethod
    def from_dict(data: dict):
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
            raise ValueError("type should be 'cities'")
        CoveredArea.__init__(self, name=name, type=type)
        self.cities = cities

    @staticmethod
    def from_dict(data: dict):
        cities = [City.from_dict(city) for city in data["cities"]]
        return Cities(cities=cities, name=data["name"], type=data["type"])

    def __str__(self) -> str:
        return f"{self.name} ({self.cities})"

    def __repr__(self) -> str:
        return f"Cities(cities={self.cities}, name={self.name}, type={self.type})"


class Region(CoveredArea):
    def __init__(self, region: str, name: str, type: str) -> None:
        if type != "region":
            raise ValueError("type should be 'region'")
        CoveredArea.__init__(self, name=name, type=type)
        self.region = region

    @staticmethod
    def from_dict(data: dict):
        return Region(region=data["region"], name=data["name"], type=data["type"])

    def __str__(self) -> str:
        return f"{self.name} ({self.region})"

    def __repr__(self) -> str:
        return f"Region(region={self.region}, name={self.name}, type={self.type})"


class Country(CoveredArea):
    def __init__(self, country: str, name: str, type: str) -> None:
        if type != "country":
            raise ValueError("type should be 'country'")
        CoveredArea.__init__(self, name=name, type=type)
        self.country = country

    @staticmethod
    def from_dict(data: dict):
        return Country(country=data["country"], name=data["name"], type=data["type"])

    def __str__(self) -> str:
        return f"{self.name} ({self.country})"

    def __repr__(self) -> str:
        return f"Country(country={self.country}, name={self.name}, type={self.type})"


class AOM(CoveredArea):
    """Autorité organisatrice des mobilités (AOM)"""

    def __init__(self, aom: AOMShortRef, name: str, type: str) -> None:
        if type != "aom":
            raise ValueError("type should be 'aom'")
        CoveredArea.__init__(self, name=name, type=type)
        self.aom = aom

    @staticmethod
    def from_dict(data: dict):
        return AOM(
            aom=AOMShortRef.from_dict(data["aom"]), name=data["name"], type=data["type"]
        )

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"AOM(aom={self.aom}, name={self.name}, type={self.type})"
