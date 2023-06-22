def is_balanced(string):
    check = 0

    for char in string:
        if char == "(":
            check += 1
        else:
            check -= 1

    if check == 0:
        return True
    else:
        return False


def is_correct_bracket(string):
    stack = []
    check = True
    for char in string:
        if char == "(":
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                check = False
                break

    return check


def solution(p):
    u, v = "", ""
    answer = ""
    if len(p) == 0 or is_correct_bracket(p):
        return p

    for i in range(2, len(p) + 1, 2):
        if is_balanced(p[:i]):
            u, v = p[:i], p[i:]
            break

    if is_correct_bracket(u):
        answer += u + solution(v)
    else:
        answer += "(" + solution(v) + ")"
        for char in u[1:-1]:
            if char == "(":
                answer += ")"
            else:
                answer += "("
    return answer


print(solution("))))(((("))
