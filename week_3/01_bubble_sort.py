input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    # 이 부분을 채워보세요!  # O(N^2)
    n = len(array)
    for i in range(n-1): # n의 길이
        for j in range(n - i - 1): # n의 길이
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!