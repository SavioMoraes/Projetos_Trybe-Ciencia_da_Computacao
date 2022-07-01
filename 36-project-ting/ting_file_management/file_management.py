import sys


def txt_importer(path_file):
    extension_file = path_file.split('.')
    if extension_file[1] != "txt":
        sys.stderr.write("Formato inválido\n")
    else:
        try:
            with open(path_file, 'r') as file:
                text = file.read().strip('').split('\n')
            return text
        except FileNotFoundError:
            sys.stderr.write(f"Arquivo {path_file} não encontrado\n")


# print(txt_importer("statics/arquivo_teste.txt"))
