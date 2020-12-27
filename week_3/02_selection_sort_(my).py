input = [4, 6, 2, 9, 1]


def selection_sort(array):
    # 이 부분을 채워보세요!
    size = len(input)
    for i in range(size-1):
        for j in range(i, size):
            if array[j]==min(array[i:size]):
                array[i], array[j] = array[j], array[i]


    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!