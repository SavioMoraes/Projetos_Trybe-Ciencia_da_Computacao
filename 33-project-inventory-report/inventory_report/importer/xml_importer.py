import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(filepath):
        _, file_extension = filepath.split(".")
        if file_extension != "xml":
            raise ValueError("Arquivo inválido")
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
