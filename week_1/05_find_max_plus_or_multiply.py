input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    value = 0
    for element in array:   # O(N)
        if value * element > value + element :
            value *= element
        else :
            value += element
    return value


result = find_max_plus_or_multiply(input)
print(result)