from objects.geometry import *
from objects.property import *


class Feature:
    def __init__(self, geometry: Geometry, properties: Property, type: str) -> None:
        self.geometry = geometry
        self.properties = properties
        if type != "feature":
            raise ValueError(f"type should be 'feature'")
        self.type = type


class FeatureCollection:
    def __init__(self, features: list[Feature], name: str, type: str) -> None:
        self.features = features
        self.name = name
        if type != "featurecollection":
            raise ValueError(f"type should be 'featurecollection'")
        self.type = type
