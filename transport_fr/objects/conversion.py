class Conversion:
    def __init__(
        self, filesize: int, last_check_conversion_is_up_to_date: str, stable_url: str
    ) -> None:
        self.filesize = filesize
        self.last_check_conversion_is_up_to_date = last_check_conversion_is_up_to_date
        self.stable_url = stable_url

    @classmethod
    def from_dict(cls, data: dict):
        return Conversion(
            filesize=data["filesize"],
            last_check_conversion_is_up_to_date=data[
                "last_check_conversion_is_up_to_date"
            ],
            stable_url=data["stable_url"],
        )

    def __str__(self) -> str:
        s = f"Conversion {self.stable_url} last check at {self.last_check_conversion_is_up_to_date})"
        return s

    def __repr__(self) -> str:
        s = f"Conversion({self.filesize}, {self.last_check_conversion_is_up_to_date}, {self.stable_url})"
        return s


class Conversions:
    def __init__(self, geojson: Conversion = None, netex: Conversion = None) -> None:
        self.geojson = geojson
        self.netex = netex

    @classmethod
    def from_dict(cls, data: dict):
        geojson_conversion = (
            Conversion.from_dict(data["geojson"]) if "geojson" in data else None
        )
        netex_conversion = (
            Conversion.from_dict(data["netex"]) if "netex" in data else None
        )
        return Conversions(geojson=geojson_conversion, netex=netex_conversion)

    def __str__(self) -> str:
        s = f"Conversions: GeoJSON: {self.geojson}, NeTEx: {self.netex}"
        return s

    def __repr__(self) -> str:
        s = f"Conversions({self.geojson}, {self.netex})"
        return s
