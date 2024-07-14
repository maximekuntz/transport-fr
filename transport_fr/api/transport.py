import requests


class TransportAPI:
    endpoint = "https://transport.data.gouv.fr"

    def _process_request(self, endpoint: str, **args):
        r = requests.get(url=endpoint, **args)
        return r.json()
