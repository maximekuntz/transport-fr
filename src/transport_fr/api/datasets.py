from geojson import GeoJSON

from transport_fr.api.transport import TransportAPI
from transport_fr.objects.datasets import *


class DatasetsAPI(TransportAPI):
    endpoint = TransportAPI.endpoint + "/api/datasets"

    def get_all(self) -> list[DatasetSummary]:
        response = self._process_request(endpoint=self.endpoint)
        return [DatasetSummary.from_dict(dataset) for dataset in response]

    def get_details(self, id: str) -> DatasetsDetails:
        endpoint = f"{self.endpoint}/{id}"
        response = self._process_request(endpoint=endpoint)
        return DatasetsDetails.from_dict(response)

    def get_geojson(self, id: str) -> GeoJSON:
        endpoint = f"{self.endpoint}/{id}/geojson"
        response = self._process_request(endpoint=endpoint)
        return GeoJSON(response)
