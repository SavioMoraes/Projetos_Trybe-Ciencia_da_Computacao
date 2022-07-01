def test_first_string(first_string):
    # if not first_string:
    #     return False
    string_1 = {}
    for letter in first_string:
        if letter in string_1:
            string_1[letter.lower()] += 1
        else:
            string_1[letter.lower()] = 1
    return string_1


def test_second_string(second_string):
    # if not second_string:
    #     return False
    string_2 = {}
    for letter in second_string:
        if letter in string_2:
            string_2[letter.lower()] += 1
        else:
            string_2[letter.lower()] = 1
    return string_2


# def test_is_anagram(first_string, second_string):
#     if first_string == "" or second_string == "":
#         return False


def is_anagram(first_string, second_string):
    string_1 = test_first_string(first_string)
    string_2 = test_second_string(second_string)
    for _ in first_string:
        string_1
    for _ in second_string:
        string_2
    for key in string_1:
        if (
            key not in string_2
            or string_1[key] != string_2[key]
        ):
            return False
    return True


print(is_anagram("amor", "roma"))
print(is_anagram("carro", "moto"))
