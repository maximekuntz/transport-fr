from api.transport import TransportAPI


class GtfsStopsAPI(TransportAPI):
    endpoint = TransportAPI.endpoint + "/api/gtfs-stops"

    def query(self, south: float, north: float, west: float, east: float):
        params = {"south": south, "north": north, "west": west, "east": east}
        response = self._process_request(endpoint=self.endpoint, params=params)
        return response
