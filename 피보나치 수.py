def solution(n):
    answer = 1
    prev = 1
    if n == 0:
        return 0
    elif n <= 2:
        return 1

    for i in range(n - 2):
        temp = answer
        answer += prev
        prev = temp

    return answer % 1234567
