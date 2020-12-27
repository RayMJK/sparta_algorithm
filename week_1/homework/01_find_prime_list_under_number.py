input = 20
list = []

# 소수는 자기 자신과 1 외에는 아무것도 나눌 수 없다.
# 주어진 자연수 N이 소수이기 위한 필요 충분 조건은
# N이 N 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
# 수가 수를 나누면 몫이 발생하는데, 몫과 나누는 수 둘중 하나는 반드시 N의 제곱근 이하
def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    for i in range(2, number+1):
        check = 0
        for j in range(2, i):
            if i % j == 0:
                check = 1
                break
        if check == 0:
            list.append(i)
        check = 0
    return list



result = find_prime_list_under_number(input)
print(result)