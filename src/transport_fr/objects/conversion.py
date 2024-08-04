class Conversion:
    def __init__(
        self, filesize: int, last_check_conversion_is_up_to_date: str, stable_url: str
    ) -> None:
        self.filesize = filesize
        self.last_check_conversion_is_up_to_date = last_check_conversion_is_up_to_date
        self.stable_url = stable_url

    @staticmethod
    def from_dict(data: dict):
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
        s = "Conversion("
        s += f"filesize={self.filesize}, "
        s += f"last_check_conversion_is_up_to_date={self.last_check_conversion_is_up_to_date}, "
        s += f"stable_url={self.stable_url})"
        return s


class Conversions:
    def __init__(self, geojson: Conversion = None, netex: Conversion = None) -> None:
        self.geojson = geojson
        self.netex = netex

    @staticmethod
    def from_dict(data: dict):
        geojson_conversion = (
            Conversion.from_dict(data["geojson"]) if "geojson" in data else None
        )
        netex_conversion = (
            Conversion.from_dict(data["netex"]) if "netex" in data else None
        )
        return Conversions(geojson=geojson_conversion, netex=netex_conversion)

    def __str__(self) -> str:
        return f"Conversions: GeoJSON: {self.geojson}, NeTEx: {self.netex}"

    def __repr__(self) -> str:
        return f"Conversions(geojson={self.geojson}, netex{self.netex})"
