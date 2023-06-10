from collections import deque


def solution(x, y, n):
    if x == y:
        return 0
    table = [0] * (y + 1)
    que = deque()
    que.append(x)

    while que:
        nx = que.popleft()
        for i in range(3):
            if i == 0:
                px = nx * 3
            if i == 1:
                px = nx * 2
            if i == 2:
                px = nx + n
            if px > y or table[px]:
                continue
            if px == y:
                return table[nx] + 1
            que.append(px)
            table[px] = table[nx] + 1

    return -1


print(solution(10, 40, 5))
