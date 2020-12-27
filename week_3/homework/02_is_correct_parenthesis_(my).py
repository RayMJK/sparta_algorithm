s = "())()("


def is_correct_parenthesis(string):
    # 구현해보세요!
    check_open = []
    for i in range(len(s)):
        if s[i] == "(":
            check_open.append(s[i])

        elif s[i] == ")":
            if not check_open:
                return False
            check_open.pop()

    if not check_open:
        return True
    else:
        return False

print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!