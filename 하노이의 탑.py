answer = []


def hanoi(n, start, destination, via):
    if n == 1:
        answer.append([start, destination])
        return
    hanoi(n - 1, start, via, destination)
    answer.append([start, destination])
    hanoi(n - 1, via, destination, start)


def solution(n):
    global answer
    hanoi(n, 1, 3, 2)
    return answer
