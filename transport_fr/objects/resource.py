import geojson

from transport_fr.objects.conversion import *


class Payload:
    pass


class CommunityResource:
    def __init__(
        self,
        community_resource_publisher: str,
        datagouv_id: str,
        format: str,
        id: int,
        is_available: bool,
        original_url: str,
        page_url: str,
        title: str,
        type: str,
        updated: str,
        url: str,
        features: list[geojson.Feature] = [],
        filesize: int = None,
        metadata=None,
        modes: list[str] = None,
        original_resource_url: str = None,
        schema_name: str = None,
        schema_version: str = None,
    ) -> None:
        self.community_resource_publisher = community_resource_publisher
        self.datagouv_id: datagouv_id
        self.features = features
        self.filesize = filesize
        self.format = format
        self.id = id
        self.is_available = is_available
        self.metadata = metadata
        self.modes = modes
        self.original_resource_url = original_resource_url
        self.original_url = original_url
        self.page_url = page_url
        self.schema_name = schema_name
        self.schema_version = schema_version
        self.title = title
        self.type = type
        self.updated = updated
        self.url = url

    @classmethod
    def from_dict(cls, data: dict):
        features = [geojson.Feature(feature) for feature in data.get("features", [])]
        cr = CommunityResource(
            community_resource_publisher=data["community_resource_publisher"],
            datagouv_id=data["datagouv_id"],
            features=features,
            filesize=data.get("filesize"),
            format=data["format"],
            id=data["id"],
            is_available=data["is_available"],
            metadata=data.get("metadata"),
            modes=data.get("modes"),
            original_resource_url=data.get("original_resource_url"),
            original_url=data["original_url"],
            page_url=data["page_url"],
            schema_name=data.get("schema_name"),
            schema_version=data.get("schema_version"),
            title=data["title"],
            type=data["type"],
            updated=data["updated"],
            url=data["url"],
        )
        return cr

    def __str__(self) -> str:
        return f"{self.title} (id {self.id})"

    def __repr__(self) -> str:
        s = f"CommunityResource({self.title}, id {self.id}, {self.url})"
        return s


class SummarizedResource:
    def __init__(
        self,
        datagouv_id: str,
        format: str,
        id: int,
        is_available: bool,
        original_url: str,
        page_url: str,
        title: str,
        type: str,
        updated: str,
        url: str,
        features: list[geojson.Feature] = [],
        filesize: int = None,
        metadata=None,
        modes: list[str] = None,
        schema_name: str = None,
        schema_version: str = None,
    ) -> None:
        self.datagouv_id: datagouv_id
        self.features = features
        self.filesize = filesize
        self.format = format
        self.id = id
        self.is_available = is_available
        self.metadata = metadata
        self.modes = modes
        self.original_url = original_url
        self.page_url = page_url
        self.schema_name = schema_name
        self.schema_version = schema_version
        self.title = title
        self.type = type
        self.updated = updated
        self.url = url

    @classmethod
    def from_dict(cls, data: dict):
        features = [geojson.Feature(feature) for feature in data.get("features", [])]
        sr = SummarizedResource(
            datagouv_id=data["datagouv_id"],
            features=features,
            filesize=data.get("filesize"),
            format=data.get("format"),
            id=data["id"],
            is_available=data["is_available"],
            metadata=data.get("metadata"),
            modes=data.get("modes"),
            original_url=data["original_url"],
            page_url=data["page_url"],
            schema_name=data.get("schema_name"),
            schema_version=data.get("schema_version"),
            title=data["title"],
            type=data["type"],
            updated=data["updated"],
            url=data["url"],
        )
        return sr

    def __str__(self) -> str:
        return f"{self.title} (id {self.id})"

    def __repr__(self) -> str:
        s = f"SummarizedResource({self.title}, id {self.id}, {self.url})"
        return s


class DetailedResource:
    def __init__(
        self,
        conversions: Conversions,
        datagouv_id: str,
        format: str,
        id: str,
        is_available: bool,
        original_url: str,
        page_url: str,
        title: str,
        type: str,
        url: str,
        features: list[geojson.Feature] = [],
        filesize: int = None,
        metadata=None,
        modes: list[str] = None,
        schema_name: str = None,
        schema_version: str = None,
    ) -> None:
        self.conversions = conversions
        self.datagouv_id = datagouv_id
        self.features = features
        self.filesize = filesize
        self.format = format
        self.id = id
        self.is_available = is_available
        self.metadata = metadata
        self.modes = modes
        self.original_url = original_url
        self.page_url = page_url
        self.schema_name = schema_name
        self.schema_version = schema_version
        self.title = title
        self.type = type
        self.url = url

    @classmethod
    def from_dict(cls, data: dict):
        features = [geojson.Feature(feature) for feature in data.get("features", [])]
        conversions = Conversions.from_dict(data["conversions"])
        dr = DetailedResource(
            conversions=conversions,
            datagouv_id=data["datagouv_id"],
            features=features,
            filesize=data.get("filesize"),
            format=data["format"],
            id=data["id"],
            is_available=data["is_available"],
            metadata=data.get("metadata"),
            modes=data.get("modes"),
            original_url=data["original_url"],
            page_url=data["page_url"],
            schema_name=data.get("schema_name"),
            schema_version=data.get("schema_version"),
            title=data["title"],
            type=data["type"],
            url=data["url"],
        )
        return dr

    def __str__(self) -> str:
        return f"{self.title} (id {self.id})"

    def __repr__(self) -> str:
        s = f"DetailedResource({self.title}, id {self.id}, {self.url})"
        return s


class ResourceHistory:
    def __init__(
        self,
        inserted_at: str,
        last_up_to_date_at: str,
        payload: Payload,
        resource_id: int,
        updated_at: str,
        resource_latest_url: str = None,
        resource_url: str = None,
        schema_name: str = None,
        schema_version: str = None,
        title: str = None,
        uuid: str = None,
        latest_schema_version_to_date: str = None,
        permanent_url: str = None,
    ) -> None:
        self.inserted_at = inserted_at
        self.last_up_to_date_at = last_up_to_date_at
        self.latest_schema_version_to_date = latest_schema_version_to_date
        self.payload = payload
        self.permanent_url = permanent_url
        self.resource_id = resource_id
        self.resource_latest_url = resource_latest_url
        self.resource_url = resource_url
        self.schema_name = schema_name
        self.schema_version = schema_version
        self.title = title
        self.updated_at = updated_at
        self.uuid = uuid

    @classmethod
    def from_dict(cls, data: dict):
        rh = ResourceHistory(
            inserted_at=data["inserted_at"],
            last_up_to_date_at=data["last_up_to_date_at"],
            latest_schema_version_to_date=data.get("latest_schema_version_to_date"),
            payload=Payload(),
            permanent_url=data.get("permanent_url"),
            resource_id=data["resource_id"],
            resource_latest_url=data.get("resource_latest_url"),
            resource_url=data.get("resource_url"),
            schema_name=data.get("schema_name"),
            schema_version=data.get("schema_version"),
            title=data.get("title"),
            updated_at=data["updated_at"],
            uuid=data.get("uuid"),
        )
        return rh

    def __str__(self) -> str:
        return f"{self.title} (id {self.resource_id}, updated at {self.updated_at})"

    def __repr__(self) -> str:
        s = f"ResourceHistory({self.title}, id {self.resource_id}, updated at {self.updated_at}, {self.permanent_url})"
        return s
