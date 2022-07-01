from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import json
import csv
import xml.etree.ElementTree as ET


class CSVReader:
    @staticmethod
    def reader(filepath):
        with open(filepath, mode="r") as file:
            products = csv.DictReader(file)
            product_list = list(products)

        return product_list


class JSONReader:
    @staticmethod
    def reader(filepath):
        with open(filepath, mode="r") as file:
            product_list = json.load(file)

        return product_list


class XMLReader:
    @staticmethod
    def reader(filepath):
        product_list = []
        root = ET.parse(filepath).getroot()

        for child in root:
            id = child.find("id").text
            nome_do_produto = child.find("nome_do_produto").text
            nome_da_empresa = child.find("nome_da_empresa").text
            data_de_fabricacao = child.find("data_de_fabricacao").text
            data_de_validade = child.find("data_de_validade").text
            numero_de_serie = child.find("numero_de_serie").text
            instrucoes_de_armazenamento = child.find(
                "instrucoes_de_armazenamento"
            ).text

            product_list.append(
                {
                    "id": id,
                    "nome_do_produto": nome_do_produto,
                    "nome_da_empresa": nome_da_empresa,
                    "data_de_fabricacao": data_de_fabricacao,
                    "data_de_validade": data_de_validade,
                    "numero_de_serie": numero_de_serie,
                    "instrucoes_de_armazenamento": instrucoes_de_armazenamento,
                }
            )
        return product_list


class Inventory:
    result = ""

    read_methods = {
        "csv": CSVReader.reader,
        "json": JSONReader.reader,
        "xml": XMLReader.reader
    }

    @classmethod
    def import_data(self, filepath, type):
        _, file_extension = filepath.split(".")
        product_list = self.read_methods[file_extension](filepath)
        result = (
            SimpleReport.generate(product_list)
            if type == "simples"
            else CompleteReport.generate(product_list)
        )

        return result


# print(
#     Inventory.import_data("inventory_report/data/inventory.xml", "completo")
# )
# print(XMLReader.reader("inventory_report/data/inventory.xml"))
