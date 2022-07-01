from inventory_report.reports.simple_report import SimpleReport
# import json


class CompleteReport(SimpleReport):

    @classmethod
    def generate(cls, product_list):
        simple_report = SimpleReport.generate(product_list)
        company_quantity = cls.get_company_occurences(product_list)[1]
        stocked_products = ""
        for company, quantity in company_quantity.items():
            stocked_products += f"- {company}: {quantity}\n"
        return (
            f"{simple_report}"
            + "\nProdutos estocados por empresa: \n"
            + stocked_products
        )


# with open("inventory_report/data/inventory.json", mode="r") as file:
#     product_list = json.load(file)
#     print(CompleteReport.generate(product_list))
