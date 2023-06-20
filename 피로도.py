from itertools import permutations


def solution1(k, dungeons):
    answer = 0
    length = len(dungeons)
    results = [0] * length
    pathes = permutations(range(length), length)

    for path in pathes:
        stress = k
        cnt = 0
        for num in path:
            if stress < dungeons[num][0]:
                break
            else:
                stress = stress - dungeons[num][1]
                cnt += 1
        results.append(cnt)

    return max(results)


answer = 0
N = 0
visited = []


def dfs(stress, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for i in range(N):
        if stress >= dungeons[i][0] and not visited[i]:
            visited[i] = True
            dfs(stress - dungeons[i][1], cnt + 1, dungeons)
            visited[i] = False


def solution(k, dungeons):
    global visited, N
    N = len(dungeons)
    visited = [False] * N
    dfs(k, 0, dungeons)
    return answer
