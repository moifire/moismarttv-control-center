from abc import ABC, abstractmethod


class BaseImporter(ABC):

    def __init__(self, source):

        self.source = source

        self.events = []

    def update(self):

        print(f"[{self.source}] Iniciando importación...")

        html = self.download()

        self.events = self.parse(html)

        self.save()

        print(f"[{self.source}] {len(self.events)} eventos importados.")

        return self.events

    @abstractmethod
    def download(self):
        pass

    @abstractmethod
    def parse(self, html):
        pass

    def save(self):

        from database.database import Database

        db = Database()

        for event in self.events:

            db.execute(
                """
                INSERT INTO events
                (
                    date,
                    time,
                    sport,
                    competition,
                    title,
                    channel,
                    backdrop,
                    source
                )
                VALUES
                (?,?,?,?,?,?,?,?)
                """,
                (
                    event["date"],
                    event["time"],
                    event["sport"],
                    event["competition"],
                    event["title"],
                    event["channel"],
                    event.get("backdrop", ""),
                    self.source
                )
            )

        db.close()