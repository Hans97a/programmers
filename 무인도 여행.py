from collections import deque


def bfs(x, y, r, c, visited, maps):
    que = deque([(x, y)])
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    cost = int(maps[x][y])
    visited[x][y] = True

    while que:
        cx, cy = que.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] != "X":
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    cost += int(maps[nx][ny])
                    que.append([nx, ny])
    return visited, cost


def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            if maps[i][j] != "X" and not visited[i][j]:
                visited, ans = bfs(i, j, n, m, visited, maps)
                answer.append(ans)

    return sorted(answer) if answer else [-1]
