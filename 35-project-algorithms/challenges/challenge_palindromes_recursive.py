def is_palindrome_recursive(word, low_index, high_index):
    # testa se o parâmetro vem vazio
    if word == "":
        return False

    # Se houver apenas um caractere
    if (low_index == high_index):
        return True

    # Se o primeiro e o último caracteres não corresponderem
    if (word[low_index] != word[high_index]):
        return False

    # Se houver mais de dois caracteres, verifique se a
    # substring do meio também é palíndromo ou não.
    if (low_index < high_index + 1):
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    return True


# Fonte:
# https://www.geeksforgeeks.org/recursive-function-check-string-palindrome/

# print(is_palindrome_recursive("ANA", 0, len("ANA") - 1))
