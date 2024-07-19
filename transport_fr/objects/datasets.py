from transport_fr.objects.covered_area import *
from transport_fr.objects.publisher import *
from transport_fr.objects.resource import *


class DatasetSummary:
    def __init__(
        self,
        aom: AOMShortRef,
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

    @classmethod
    def from_dict(cls, data: dict):
        aom = AOMShortRef.from_dict(data["aom"])
        community_resources = [
            CommunityResource.from_dict(cr) for cr in data["community_resources"]
        ]
        covered_area = CoveredArea.from_dict(data["covered_area"])
        publisher = Publisher.from_dict(data["publisher"])
        resources = [SummarizedResource.from_dict(r) for r in data["resources"]]
        return DatasetSummary(
            aom=aom,
            community_resources=community_resources,
            covered_area=covered_area,
            created_at=data["created_at"],
            datagouv_id=data["datagouv_id"],
            id=data["id"],
            licence=data["licence"],
            page_url=data["page_url"],
            publisher=publisher,
            resources=resources,
            slug=data["slug"],
            title=data["title"],
            type=data["type"],
            updated=data.get("updated"),
        )

    def __str__(self) -> str:
        return f"{self.title} (id {self.id})"

    def __repr__(self) -> str:
        return f"DatasetSummary({self.title}, id {self.id})"


class DatasetsDetails:
    def __init__(
        self,
        aom: AOMShortRef,
        community_resources: list[CommunityResource],
        covered_area: CoveredArea,
        created_at: str,
        datagouv_id: str,
        history: list[ResourceHistory],
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

    @classmethod
    def from_dict(cls, data: dict):
        aom = AOMShortRef.from_dict(data["aom"])
        community_resources = [
            CommunityResource.from_dict(cr) for cr in data["community_resources"]
        ]
        covered_area = CoveredArea.from_dict(data["covered_area"])
        history = [ResourceHistory.from_dict(h) for h in data["history"]]
        publisher = Publisher.from_dict(data["publisher"])
        resources = [DetailedResource.from_dict(r) for r in data["resources"]]
        return DatasetsDetails(
            aom=aom,
            community_resources=community_resources,
            covered_area=covered_area,
            created_at=data["created_at"],
            datagouv_id=data["datagouv_id"],
            history=history,
            id=data["id"],
            licence=data["licence"],
            page_url=data["page_url"],
            publisher=publisher,
            resources=resources,
            slug=data["slug"],
            title=data["title"],
            type=data["type"],
            updated=data.get("updated"),
        )

    def __str__(self) -> str:
        return f"{self.title} (id {self.id})"

    def __repr__(self) -> str:
        return f"DatasetsDetails({self.title}, id {self.id})"
