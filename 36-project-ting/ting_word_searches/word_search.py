# from ting_file_management.queue import Queue
# from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    found_words = []
    for index in range(len(instance)):
        text = instance.search(index)
        lines = []

        occurrences = {
            "palavra": word,
            "arquivo": text['nome_do_arquivo'],
            "ocorrencias": lines,
        }

        if len(occurrences['ocorrencias']) == 0:
            found_words
        else:
            found_words.append(occurrences)

    return found_words


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


# print(exists_word('Pedro', Queue()))
