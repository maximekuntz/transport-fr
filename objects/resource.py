import geojson

from objects.conversion import *


class Payload:
    def __init__(self) -> None:
        pass

    @staticmethod
    def from_dict(data: dict):
        return Payload()


class CommunityResource:
    def __init__(
        self,
        community_resource_publisher: str,
        datagouv_id: str,
        features: list[geojson.Feature],
        filesize: int,
        format: str,
        id: int,
        is_available: bool,
        metadata,
        modes: list[str],
        original_resource_url: str,
        original_url: str,
        page_url: str,
        schema_name: str,
        schema_version: str,
        title: str,
        type: str,
        updated: str,
        url: str,
    ) -> None:
        self.community_resource_publisher = community_resource_publisher
        self.datagouv_id = datagouv_id
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

    def __str__(self) -> str:
        return f"{self.title} (id {self.id})"

    def __repr__(self) -> str:
        s = "CommunityResource("
        s += f"community_resource_publisher={self.community_resource_publisher}, "
        s += f"datagouv_id={self.datagouv_id}, "
        s += f"features={self.features}, "
        s += f"filesize={self.filesize}, "
        s += f"format={self.format}, "
        s += f"id={self.id}, "
        s += f"is_available={self.is_available}, "
        s += f"metadata={self.metadata}, "
        s += f"modes={self.modes}, "
        s += f"original_resource_url={self.original_resource_url}, "
        s += f"original_url={self.original_url}, "
        s += f"page_url={self.page_url}, "
        s += f"schema_name={self.schema_name}, "
        s += f"schema_version={self.schema_version}, "
        s += f"title={self.title}, "
        s += f"type={self.type}, "
        s += f"updated={self.updated}, "
        s += f"url={self.url})"
        return s


class SummarizedResource:
    def __init__(
        self,
        datagouv_id: str,
        features: list[geojson.Feature],
        filesize: int,
        format: str,
        id: int,
        is_available: bool,
        metadata,
        modes: list[str],
        original_url: str,
        page_url: str,
        schema_name: str,
        schema_version: str,
        title: str,
        type: str,
        updated: str,
        url: str,
    ) -> None:
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
        self.updated = updated
        self.url = url

    def __str__(self) -> str:
        return f"{self.title} (id {self.id})"

    def __repr__(self) -> str:
        s = "SummarizedResource("
        s += f"datagouv_id={self.datagouv_id}, "
        s += f"format={self.format}, "
        s += f"id= {self.id}, {self.url})"
        s += f"is_available={self.is_available}, "
        s += f"original_url={self.original_url}, "
        s += f"page_url={self.page_url}, "
        s += f"title={self.title}, "
        s += f"type={self.type}, "
        s += f"updated={self.updated}, "
        s += f"url={self.url}, "
        s += f"features={self.features}, "
        s += f"filesize={self.filesize}, "
        s += f"metadata={self.metadata}, "
        s += f"modes={self.modes}, "
        s += f"schema_name={self.schema_name}, "
        s += f"schema_version={self.schema_version})"
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
        features: list[geojson.Feature] = None,
        filesize: int = None,
        metadata=None,
        modes: list[str] = None,
        schema_name: str = None,
        schema_version: str = None,
    ) -> None:
        if features is None:
            features = []
        if modes is None:
            modes = []
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

    def __str__(self) -> str:
        return f"{self.title} (id {self.id})"

    def __repr__(self) -> str:
        s = "DetailedResource("
        s += f"conversions={self.conversions}, "
        s += f"datagouv_id={self.datagouv_id}, "
        s += f"features={self.features}, "
        s += f"filesize={self.filesize}, "
        s += f"format={self.format}, "
        s += f"id={self.id}, "
        s += f"is_available={self.is_available}, "
        s += f"metadata={self.metadata}, "
        s += f"modes={self.modes}, "
        s += f"original_url={self.original_url}, "
        s += f"page_url={self.page_url}, "
        s += f"schema_name={self.schema_name}, "
        s += f"schema_version={self.schema_version}, "
        s += f"title={self.title}, "
        s += f"type={self.type}, "
        s += f"url={self.url})"
        return s


class ResourceHistory:
    def __init__(
        self,
        inserted_at: str,
        last_up_to_date: str,
        latest_schema_version_to_date: str,
        payload: Payload,
        permanent_url: str,
        resource_id: int,
        resource_latest_url: str,
        resource_url: str,
        schema_name: str,
        schema_version: str,
        title: str,
        updated_at: str,
        uuid: str,
    ) -> None:
        self.inserted_at = inserted_at
        self.last_up_to_date = last_up_to_date
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

    def __str__(self) -> str:
        return f"{self.title} (id {self.resource_id}, updated at {self.updated_at})"

    def __repr__(self) -> str:
        s = "ResourceHistory("
        s += f"inserted_at={self.inserted_at}, "
        s += f"last_up_to_date_at={self.last_up_to_date_at}, "
        s += f"latest_schema_version_to_date={self.latest_schema_version_to_date}, "
        s += f"payload={self.payload}, "
        s += f"permanent_url={self.permanent_url}, "
        s += f"resource_id={self.resource_id}, "
        s += f"resource_latest_url={self.resource_latest_url}, "
        s += f"resource_url={self.resource_url}, "
        s += f"schema_name={self.schema_name}, "
        s += f"schema_version={self.schema_version}, "
        s += f"title={self.title}, "
        s += f"updated_at={self.updated_at}, "
        s += f"uuid={self.uuid})"
        return s
