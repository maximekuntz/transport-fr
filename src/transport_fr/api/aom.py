from geojson import GeoJSON

from transport_fr.api.transport import TransportAPI
from transport_fr.objects.aom import AOMResponse


class AOMAPI(TransportAPI):
    endpoint = TransportAPI.endpoint + "/api/aoms"

    def from_coordinates(self, lon: float, lat: float) -> AOMResponse:
        params = {"lon": lon, "lat": lat}
        response = self._process_request(endpoint=self.endpoint, params=params)
        return AOMResponse.from_dict(response)

    def from_insee_code(self, insee_code: int) -> AOMResponse:
        endpoint = f"{self.endpoint}/{insee_code}"
        response = self._process_request(endpoint=endpoint)
        return AOMResponse.from_dict(response)

    def get_all(self) -> GeoJSON:
        endpoint = f"{self.endpoint}/geojson"
        response = self._process_request(endpoint=endpoint)
        return GeoJSON(response)
