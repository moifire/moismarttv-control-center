from abc import ABC, abstractmethod
from datetime import datetime


class BaseImporter(ABC):

    def __init__(self, source):

        self.source = source

        self.events = []

    def update(self):

        print("=" * 60)
        print(f"Iniciando importador: {self.source}")
        print("=" * 60)

        html = self.download()

        if not html:
            print("No se pudo descargar contenido.")
            return []

        self.events = self.parse(html)

        print(f"Eventos encontrados: {len(self.events)}")

        return self.events

    @abstractmethod
    def download(self):
        pass

    @abstractmethod
    def parse(self, html):
        pass

    def build_event(
        self,
        date="",
        time="",
        sport="",
        competition="",
        title="",
        channel="",
        backdrop=""
    ):

        return {
            "date": date,
            "time": time,
            "sport": sport,
            "competition": competition,
            "title": title,
            "channel": channel,
            "backdrop": backdrop,
            "source": self.source,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }