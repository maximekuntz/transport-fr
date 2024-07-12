from api.transport import TransportAPI
from objects.datasets import *


class DatasetsAPI(TransportAPI):
    endpoint = TransportAPI.endpoint + "/api/datasets"

    def get_all(self) -> list[DatasetSummary]:
        response = self._process_request(endpoint=self.endpoint)
        datasets = [DatasetSummary(**dataset) for dataset in response]
        return datasets

    def get_details(self, id: str) -> DatasetsDetails:
        endpoint = f"{self.endpoint}/{id}"
        response = self._process_request(endpoint=endpoint)
        dataset = DatasetsDetails(**response)
        return dataset

    def get_geojson(self, id: str):
        endpoint = f"{self.endpoint}/{id}/geojson"
        response = self._process_request(endpoint=endpoint)
        return response
