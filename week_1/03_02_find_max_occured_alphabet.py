input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!

    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    max_number = max(alphabet_occurrence_array)
    max_index = alphabet_occurrence_array.index(max_number)

    return chr((ord('a')+max_index))


result = find_max_occurred_alphabet(input)
print(result)