def solution(s):
    stack = []
    for gwalho in s:
        if gwalho == "(":
            stack.append("(")
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0
