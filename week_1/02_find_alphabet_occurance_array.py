def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char)-ord("a")
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array



'''
    # 나의 코드
    for i in string:
        if i.isalpha() == True:
            alphabet_occurrence_array[(ord(i)-ord('a'))]+=1
        else:
            continue
    return alphabet_occurrence_array
'''

print(find_alphabet_occurrence_array("hello my name is sparta"))