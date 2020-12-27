input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    # 이 부분을 채워보세요!
    size=len(input)
    while size-1 > 0:
        size -= 1
        n = 0
        for i in range(len(input)-n-1):
            n+=1
            if input[i] > input[i+1]:
                input[i], input[i+1] = input[i+1], input[i]

    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!