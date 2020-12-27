# Factorial(N) = N * Factorial(N-1)
# ....
# Factorial(1) = 1

def factorial(n):
    # 이 부분을 채워보세요!
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(5))