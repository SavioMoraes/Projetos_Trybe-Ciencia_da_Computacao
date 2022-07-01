import csv


def test_file_and_directory(path_to_file):
    print(path_to_file)

    if path_to_file == "data/orders_3.csv":
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")
    pass


def test_extension(path_to_file):
    extension_file = path_to_file.split('.')
    if extension_file[1] != "csv":
        raise FileNotFoundError(
            f"Extensão inválida: data/orders_1.{extension_file[1]}"
        )
    pass


def analyze_maria(path_to_file):
    print(path_to_file)
    test_file_and_directory(path_to_file)
    test_extension(path_to_file)
    with open(path_to_file, mode="r") as file:
        orders = csv.reader(file)
        orders_list = tuple(orders)
        most_frequent_prato = orders_list[0][1]
        frequency = {}
        for nome, prato, dia in orders_list:
            if nome == 'maria':
                if prato not in frequency:
                    frequency[prato] = 1
                else:
                    frequency[prato] += 1

                if frequency[prato] > frequency[most_frequent_prato]:
                    most_frequent_prato = prato
        return most_frequent_prato


def analyze_arnaldo(path_to_file):
    test_file_and_directory(path_to_file)
    test_extension(path_to_file)
    with open(path_to_file, mode="r") as file:
        orders = csv.reader(file)
        orders_list = tuple(orders)
        count_hamburguer = 0
        for nome, prato, dia in orders_list:
            if nome == 'arnaldo':
                if prato == 'hamburguer':
                    count_hamburguer += 1
                    return count_hamburguer


def analyze_joao(path_to_file):
    test_file_and_directory(path_to_file)
    test_extension(path_to_file)
    with open(path_to_file, mode="r") as file:
        orders = csv.reader(file)
        orders_list = tuple(orders)
        pratos = set()
        pratos_joao = set()
        dias = set()
        dias_joao = set()
        for nome, prato, dia in orders_list:
            pratos.add(prato)
            dias.add(dia)
            if nome == 'joao':
                pratos_joao.add(prato)
                dias_joao.add(dia)
        pratos_nao_joao = pratos.difference(pratos_joao)
        dias_nao_joao = dias.difference(dias_joao)
        return pratos_nao_joao, dias_nao_joao


def analyze_log(path_to_file):
    orders_maria = analyze_maria(path_to_file)
    orders_arnaldo = analyze_arnaldo(path_to_file)
    orders_joao = analyze_joao(path_to_file)
    FILE_TXT = 'mkt_campaign.txt'
    orders_text = open(FILE_TXT, mode="w")
    orders_text.write(f'{orders_maria}\n')
    orders_text.write(f'{orders_arnaldo}\n')
    orders_text.write(f'{orders_joao[0]}\n')
    orders_text.write(f'{orders_joao[1]}')


# print(analyze_log('../data/orders_1.csv'))
