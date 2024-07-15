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

    @staticmethod
    def from_dict(data: dict):
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
        s = "DatasetSummary("
        s += f"aom={self.aom}, "
        s += f"community_resources={self.community_resources}, "
        s += f"covered_area={self.covered_area}, "
        s += f"created_at={self.created_at}, "
        s += f"datagouv_id={self.datagouv_id}, "
        s += f"id={self.id}, "
        s += f"licence={self.licence}, "
        s += f"page_url={self.page_url}, "
        s += f"publisher={self.publisher}, "
        s += f"resources={self.resources}, "
        s += f"slug={self.slug}, "
        s += f"title={self.title}, "
        s += f"type={self.type}, "
        s += f"updated={self.updated})"
        return s


class DatasetsDetails:
    def __init__(
        self,
        aom: AOMShortRef,
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

    @staticmethod
    def from_dict(data: dict):
        aom = AOMShortRef.from_dict(data["aom"])
        community_resources = [
            CommunityResource.from_dict(cr) for cr in data["community_resources"]
        ]
        covered_area = CoveredArea.from_dict(data["covered_area"])
        history = ResourceHistory.from_dict(data["history"])
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
        s = "DatasetsDetails("
        s += f"aom={self.aom}, "
        s += f"community_resources={self.community_resources}, "
        s += f"covered_area={self.covered_area}, "
        s += f"created_at={self.created_at}, "
        s += f"datagouv_id={self.datagouv_id}, "
        s += f"history={self.history}, "
        s += f"id={self.id}, "
        s += f"licence={self.licence}, "
        s += f"page_url={self.page_url}, "
        s += f"publisher={self.publisher}, "
        s += f"resources={self.resources}, "
        s += f"slug={self.slug}, "
        s += f"title={self.title}, "
        s += f"type={self.type}, "
        s += f"updated={self.updated})"
        return s
