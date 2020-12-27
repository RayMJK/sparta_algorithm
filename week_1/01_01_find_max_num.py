input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 이 부분을 채워보세요!
    for num in array:
        for compare_num in array:

            if num < compare_num :
                break

        else :              # for문이 다 끝날때까지 break 부분이 한번도 실 나오지 않았다면 실행
            return num


'''
    max = 0
    for i in input:
        if max < i:
            max = i


    return max
'''

result = find_max_num(input)
print(result)