from geojson import GeoJSON

from transport_fr.api.transport import TransportAPI
from transport_fr.objects.covered_area import AOM


class AOMAPI(TransportAPI):
    endpoint = TransportAPI.endpoint + "/api/aoms"

    def from_coordinates(self, lon: float, lat: float) -> AOM:
        params = {"lon": lon, "lat": lat}
        response = self._process_request(endpoint=self.endpoint, params=params)
        aom = AOM(**response)
        return aom

    def from_insee_code(self, insee_code: int) -> AOM:
        endpoint = f"{self.endpoint}/{insee_code}"
        response = self._process_request(endpoint=endpoint)
        aom = AOM(**response)
        return aom

    def get_all(self) -> GeoJSON:
        endpoint = f"{self.endpoint}/geojson"
        response = self._process_request(endpoint=endpoint)
        gjson = GeoJSON(response)
        return gjson
