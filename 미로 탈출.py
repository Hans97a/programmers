"""
아래 주석된 코드는 스택 자료구조를 이용하여 가능한 모든 경로를 탐색하고 그 중 작은 값을 리턴하도록 시도한 코드.
테스트 케이스는 경로가 하나 밖에 나오지 않아 성공이지만 제출 시 미로를 탈출하는 여러 경로가 존재하고,
그 중 사이클이 존재할 경우 RecursionError 발생하여 오답
"""


"""
answer = []
stack = []
len_w = 0
len_h = 0


def find_S(maps):
    global len_w, len_h
    for i in range(len_h):
        for j in range(len_w):
            if maps[i][j] == "S":
                return [i, j]


def can_go(maps, i, j):
    if maps[i][j] in ["L", "O", "E"]:
        return True
    return False


def dfs(maps, i, j, cnt, before_i, before_j):
    global len_w, len_h, answer, stack

    if maps[i][j] == "E":
        answer.append(cnt)
        return

    if stack:
        i, j, cnt, b_i, b_j = stack.pop()
        dfs(maps, i, j, cnt, b_i, b_j)
    else:
        if i - 1 >= 0 and can_go(maps, i - 1, j) and before_i != i - 1:  # 위쪽
            stack.append([i - 1, j, cnt + 1, i, j])
        if i + 1 <= len_h - 1 and can_go(maps, i + 1, j) and before_i != i + 1:  # 아래쪽
            stack.append([i + 1, j, cnt + 1, i, j])
        if j - 1 >= 0 and can_go(maps, i, j - 1) and before_j != j - 1:  # 왼쪽
            stack.append([i, j - 1, cnt + 1, i, j])
        if j + 1 <= len_w - 1 and can_go(maps, i, j + 1) and before_j != j + 1:  # 오른쪽
            stack.append([i, j + 1, cnt + 1, i, j])

        if stack:
            tmp_i, tmp_j, cnt, b_i, b_j = stack.pop()
            dfs(maps, tmp_i, tmp_j, cnt, b_i, b_j)
        else:
            if cnt > 3:
                answer.append(cnt + 1)


def solution(maps):
    global answer, len_w, len_h
    len_w = len(maps[0])
    len_h = len(maps)
    i, j = find_S(maps)

    dfs(maps, i, j, 0, i, j)

    return min(answer) if answer else -1
"""


from collections import deque


def bfs(start, end, maps):
    # 탐색할 방향
    dy = [0, 1, -1, 0]
    dx = [1, 0, 0, -1]

    n = len(maps)  # 세로
    m = len(maps[0])  # 가로
    visited = [[False] * m for _ in range(n)]
    que = deque()
    flag = False

    # 초깃값 설정
    for i in range(n):
        for j in range(m):
            # 출발하고자 하는 지점이라면 시작점의 좌표를 기록함
            if maps[i][j] == start:
                que.append((i, j, 0))
                # 별도의 cost 리스트를 만들지 않고 que에 바로 기록(0)
                visited[i][j] = True
                flag = True
                break
                # 시작 지점은 한 개만 존재하기 때문에 찾으면 바로 나옴
        if flag:
            break

    # BFS 알고리즘 수행 (핵심)
    while que:
        y, x, cost = que.popleft()

        if maps[y][x] == end:
            return cost

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            # maps 범위내에서 벽이 아니라면 지나갈 수 있음
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != "X":
                if not visited[ny][nx]:  # 아직 방문하지 않는 통로라면
                    que.append((ny, nx, cost + 1))
                    visited[ny][nx] = True

    return -1  # 탈출할 수 없다면


def solution(maps):
    path1 = bfs("S", "L", maps)  # 시작 지점 --> 레버
    path2 = bfs("L", "E", maps)  # 레버 --> 출구

    # 둘다 -1 이 아니라면 탈출할 수 있음
    if path1 != -1 and path2 != -1:
        return path1 + path2

    # 둘중 하나라도 -1 이면 탈출할 수 없음
    return -1


print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXO", "OOOOE"]))
