from datetime import date
from abc import ABC, abstractmethod


class Serializer(ABC):
    @abstractmethod
    def serialize(cls, product_list):
        raise NotImplementedError


class SimpleReport(Serializer):
    @classmethod
    def get_company_occurences(cls, product_list):
        company_occurences = dict()
        company_most_occurrence = ""
        for product in product_list:
            if product["nome_da_empresa"] in company_occurences:
                company_occurences[product["nome_da_empresa"]] += 1
            else:
                company_occurences[product["nome_da_empresa"]] = 1
        number_of_company = company_occurences[
            max(company_occurences, key=company_occurences.get)
        ]
        for company, occurrence in company_occurences.items():
            if occurrence == number_of_company:
                company_most_occurrence = company
        return [company_most_occurrence, company_occurences]

    @classmethod
    def generate(cls, product_list):
        company = cls.get_company_occurences(product_list)[0]
        current_date = date.today()
        oldest_date = current_date
        validation_date = "initial_value"
        for product in product_list:
            fabrication_date = product["data_de_fabricacao"]
            expired_date = product["data_de_validade"]
            if date.fromisoformat(fabrication_date) < oldest_date:
                oldest_date = date.fromisoformat(fabrication_date)
            if (
                date.fromisoformat(expired_date) > current_date
                and validation_date == "initial_value"
            ):
                validation_date = date.fromisoformat(expired_date)
                continue
            if (
                validation_date
                > date.fromisoformat(expired_date)
                > current_date
            ):
                validation_date = date.fromisoformat(expired_date)

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            + f"Data de validade mais próxima: {validation_date}\n"
            + f"Empresa com maior quantidade de produtos estocados: {company}"
            + "\n"
        )
