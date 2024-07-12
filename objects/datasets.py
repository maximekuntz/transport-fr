from objects.covered_area import *
from objects.publisher import *
from objects.resource import *


class DatasetSummary:
    def __init__(
        self,
        aom: AOM,
        community_resources: list[CommunityResource],
        covered_area: CoveredArea,
        created_at: str,
        datagouv_id: str,
        id: str,
        licence: str,
        page_url: str,
        publisher: Publisher,
        resources: list[CommunityResource | SummarizedResource],
        slug: str,
        title: str,
        type: str,
        updated: str = None,
    ) -> None:
        self.aom = aom
        self.community_resources = community_resources
        self.covered_area = covered_area
        self.created_at = created_at
        self.datagouv_id = datagouv_id
        self.id = id
        self.licence = licence
        self.page_url = page_url
        self.publisher = publisher
        self.slug = slug
        self.title = title
        self.type = type
        self.resources = resources
        self.updated = updated

    def __str__(self) -> str:
        return f"{self.title} (id {self.id})"

    def __repr__(self) -> str:
        return f"DatasetSummary({self.title}, id {self.id})"


class DatasetsDetails:
    def __init__(
        self,
        aom: AOM,
        community_resources: list[CommunityResource],
        covered_area: CoveredArea,
        created_at: str,
        datagouv_id: str,
        history: ResourceHistory,
        id: str,
        licence: str,
        page_url: str,
        publisher: Publisher,
        resources: list[CommunityResource | DetailedResource],
        slug: str,
        title: str,
        type: str,
        updated: str = None,
    ) -> None:
        self.aom = aom
        self.community_resources = community_resources
        self.covered_area = covered_area
        self.created_at = created_at
        self.datagouv_id = datagouv_id
        self.history = history
        self.id = id
        self.licence = licence
        self.page_url = page_url
        self.publisher = publisher
        self.slug = slug
        self.title = title
        self.type = type
        self.resources = resources
        self.updated = updated

    def __str__(self) -> str:
        return f"{self.title} (id {self.id})"

    def __repr__(self) -> str:
        return f"DatasetsDetails({self.title}, id {self.id})"
