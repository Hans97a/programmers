"""
[5, 5, 5], ["diamond"] * 50
다른 테스트 케이스는 모두 제한시간 내에 처리 가능하나 위 테스트 케이스의 경우
매우 많은 시간이 소요되므로 (시간 복잡도 : O(total*len(minerals))) 탈락
"""

# DFS 풀이

# lookup = dict()
# stress = float("inf")


# def mining(order, minerals):
#     global stress
#     i = 0
#     mineral_len = len(minerals)
#     result = 0
#     for pick in order:
#         pick = int(pick)
#         duration_cnt = 0
#         for j in range(i, mineral_len):
#             if duration_cnt == 5:
#                 break
#             mineral = minerals[j]
#             if pick == 0:
#                 result += 1
#             elif pick == 1:
#                 if mineral == "diamond":
#                     result += 5
#                 else:
#                     result += 1
#             else:
#                 if mineral == "diamond":
#                     result += 25
#                 elif mineral == "iron":
#                     result += 5
#                 else:
#                     result += 1
#             duration_cnt += 1
#         i = j
#         if i == mineral_len - 1:
#             break
#     stress = min(stress, result)


# def dfs(minerals, order, total, temp_picks):
#     global lookup

#     if len(order) == total:
#         try:
#             lookup[order]
#         except:
#             mining(order, minerals)
#             lookup[order] = 0
#         return
#     for i in range(3):
#         if temp_picks[i] != 0:
#             order += str(i)
#             temp_picks[i] -= 1
#             dfs(minerals, order, total, temp_picks)
#             order = order[:-1]
#             temp_picks[i] += 1


# def solution(picks, minerals):
#     global stress
#     dfs(minerals, "", sum(picks), picks)
#     return stress


# 큐 구현 예제

from collections import deque


def solution(picks, minerals):
    answer = 0
    tiredList = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    connectionDict = {"diamond": 0, "iron": 1, "stone": 2}
    info = []
    minerals = minerals[: 5 * sum(picks)]
    q = deque(minerals)
    while q:
        howManyDig = 0
        usedDia, usedIron, usedStone = 0, 0, 0
        while howManyDig < 5:
            howManyDig += 1
            mineral = q.popleft()
            usedDia += tiredList[0][connectionDict[mineral]]
            usedIron += tiredList[1][connectionDict[mineral]]
            usedStone += tiredList[2][connectionDict[mineral]]
            if not q:
                break
        info.append([usedDia, usedIron, usedStone])
    info.sort(key=lambda x: [x[2], x[1], x[0]])

    for idx, p in enumerate(picks):
        for _ in range(p):
            if info:
                answer += info.pop()[idx]
            else:
                break
    return answer


print(
    solution(
        [1, 3, 2],
        ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"],
    )
)
