input = "abacabade"


def find_not_repeating_character(string):
    # 이 부분을 채워보세요!
    list=[]
    for element in string:
        if element in list :
            list.remove(element)
        else :
            list.append(element)

    if not list :
        return "_"
    return list[0]


result = find_not_repeating_character(input)
print(result)