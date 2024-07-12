from api.transport import TransportAPI
from objects.feature import FeatureCollection


class StatsAPI(TransportAPI):
    endpoint = TransportAPI.endpoint + "/api/stats"

    def covered_regions(self):
        response = self._process_request(endpoint=self.endpoint)
        fc = FeatureCollection(**response)
        return fc

    def regions(self):
        endpoint = f"{self.endpoint}/regions"
        response = self._process_request(endpoint=endpoint)
        fc = FeatureCollection(**response)
        return fc

    def bike_scooter_sharing(self):
        endpoint = f"{self.endpoint}/bike-scooter-sharing"
        response = self._process_request(endpoint=endpoint)
        fc = FeatureCollection(**response)
        return fc

    def quality(self):
        endpoint = f"{self.endpoint}/quality"
        response = self._process_request(endpoint=endpoint)
        fc = FeatureCollection(**response)
        return fc
