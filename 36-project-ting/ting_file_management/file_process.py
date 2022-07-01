import sys
# from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    text = txt_importer(path_file)

    result = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(text),
            'linhas_do_arquivo': text,
    }

    if result in instance._data:
        return None

    instance.enqueue(result)
    print(f"{result}", file=sys.stdout)


def remove(instance):
    if instance.is_empty():
        return print('Não há elementos', file=sys.stdout)
    data = instance.dequeue()
    print(f"Arquivo {data['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        search_index = instance.search(position)
        print(f"{search_index}", file=sys.stdout)
    except IndexError:
        sys.stderr.write("Posição inválida\n")


# print(process("statics/arquivo_teste.txt", Queue()))
