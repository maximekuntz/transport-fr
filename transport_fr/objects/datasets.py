from transport_fr.objects.covered_area import *
from transport_fr.objects.publisher import *
from transport_fr.objects.resource import *


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
