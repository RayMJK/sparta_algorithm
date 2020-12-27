input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 이 부분을 채워보세요!
    max = 0
    for i in input:
        if max < i:
            max = i


    return max


result = find_max_num(input)
print(result)