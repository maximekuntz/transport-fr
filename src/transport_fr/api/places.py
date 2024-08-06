from transport_fr.api.transport import TransportAPI
from transport_fr.objects.places import *


class PlacesAPI(TransportAPI):
    endpoint = TransportAPI.endpoint + "/api/places"

    def query(self, q: str) -> list[Place]:
        params = {"q": q}
        response = self._process_request(endpoint=self.endpoint, params=params)
        return [Place.from_dict(place) for place in response]
