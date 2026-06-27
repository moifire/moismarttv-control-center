import os
import requests
from bs4 import BeautifulSoup

from .base import BaseImporter


class FutbolEnLaTVImporter(BaseImporter):

    URL = "https://www.futbolenlatv.es/deporte"

    def __init__(self):

        super().__init__("FutbolEnLaTV")

    def download(self):

        print("Descargando FutbolEnLaTV...")

        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        r = requests.get(
            self.URL,
            headers=headers,
            timeout=30
        )

        r.raise_for_status()

        os.makedirs("cache", exist_ok=True)

        with open(
            "cache/futbolenlatv.html",
            "w",
            encoding="utf8"
        ) as f:

            f.write(r.text)

        return r.text

    def parse(self, html):

        soup = BeautifulSoup(html, "html.parser")

        print("Título:", soup.title.text if soup.title else "Sin título")

        events = []

        #
        # El parser real se implementará
        # en el Commit 4.2
        #

        return events