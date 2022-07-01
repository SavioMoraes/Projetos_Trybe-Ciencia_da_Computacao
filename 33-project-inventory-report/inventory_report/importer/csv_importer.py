import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(filepath):
        _, file_extension = filepath.split(".")
        if file_extension != "csv":
            raise ValueError("Arquivo inválido")
        with open(filepath, mode="r") as file:
            products = csv.DictReader(file)
            product_list = list(products)

        return product_list
