import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(filepath):
        _, file_extension = filepath.split(".")
        if file_extension != "json":
            raise ValueError("Arquivo inválido")
        with open(filepath, mode="r") as file:
            product_list = json.load(file)

        return product_list
