import requests

from .base import BaseImporter


class FutbolEnLaTVImporter(BaseImporter):

    URL = "https://www.futbolenlatv.es/deporte"

    def __init__(self):

        super().__init__("FutbolEnLaTV")

    def download(self):

        print("Descargando FutbolEnLaTV...")

        response = requests.get(
            self.URL,
            timeout=20,
            headers={
                "User-Agent":
                "Mozilla/5.0"
            }
        )

        return response.text

    def parse(self, html):

        print("Parser pendiente...")

        return []