from modules.importers.futbolenlatv import FutbolEnLaTVImporter


class AgendaService:

    @staticmethod
    def update():

        importer = FutbolEnLaTVImporter()

        return importer.update()