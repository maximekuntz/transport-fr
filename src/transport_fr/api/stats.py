from geojson import FeatureCollection

from transport_fr.api.transport import TransportAPI


class StatsAPI(TransportAPI):
    endpoint = TransportAPI.endpoint + "/api/stats"

    def covered_regions(self) -> FeatureCollection:
        response = self._process_request(endpoint=self.endpoint)
        return FeatureCollection(**response)

    def regions(self) -> FeatureCollection:
        endpoint = f"{self.endpoint}/regions"
        response = self._process_request(endpoint=endpoint)
        return FeatureCollection(**response)

    def bike_scooter_sharing(self) -> FeatureCollection:
        endpoint = f"{self.endpoint}/bike-scooter-sharing"
        response = self._process_request(endpoint=endpoint)
        return FeatureCollection(**response)

    def quality(self) -> FeatureCollection:
        endpoint = f"{self.endpoint}/quality"
        response = self._process_request(endpoint=endpoint)
        return FeatureCollection(**response)
