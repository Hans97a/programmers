"""
테스트 케이스 4의 경우 어피치에게 점수가 밀리는 경우에 대한 케이스를 커버하기 어려운 코드
"""

# answer = []
# arr = [0 for i in range(11)]
# scores = [i for i in range(10, -1, -1)]
# maximum_score = 0


# def dfs(cnt, n, info):
#     global arr, scores, maximum_score, answer
#     if cnt > n:
#         return

#     lion_score = sum([scores[i] for i, shot in enumerate(arr) if shot > info[i]])
#     apeach_score = sum(
#         [scores[i] for i, shot in enumerate(info) if shot >= arr[i] and shot != 0]
#     )
#     if cnt == n:
#         if maximum_score <= lion_score and apeach_score < lion_score:
#             maximum_score = lion_score
#             answer.append([lion_score] + arr)

#             to_remove = []
#             for i, array in enumerate(answer):
#                 if array[0] < lion_score:
#                     to_remove.append(i)

#             if to_remove:
#                 temp_answer = []
#                 for i in range(len(answer)):
#                     if i not in to_remove:
#                         temp_answer.append(answer[i])
#                 answer = temp_answer.copy()
#         return

#     for i in range(n):
#         if arr[i] <= info[i]:
#             shot_cnt = info[i] + 1 - arr[i]
#             arr_temp = arr[i]
#             arr[i] = info[i] + 1
#             dfs(cnt + shot_cnt, n, info)
#             arr[i] = arr_temp


# def solution(n, info):
#     global answer, scores

#     dfs(0, n, info)
#     print(answer)
#     if answer:
#         return answer[-1][1:]
#     else:
#         return [-1]


from collections import deque


def bfs(n, info):
    result = []
    que = deque([(0, [0 for i in range(11)])])
    maximum_gap = 0

    while que:
        index, arrows = que.popleft()
        arrow_sum = sum(arrows)

        if arrow_sum == n:
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrows[i] == 0):
                    if info[i] >= arrows[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:
                gap = lion - apeach
                if maximum_gap > gap:
                    continue
                elif maximum_gap < gap:
                    maximum_gap = gap
                    result.clear()
                result.append(arrows)

        elif arrow_sum > n:
            continue
        elif index == 10:
            temp = arrows.copy()
            temp[index] = n - sum(temp)
            que.append((-1, temp))
        else:
            temp = arrows.copy()
            temp[index] = info[index] + 1
            que.append((index + 1, temp))
            temp = arrows.copy()
            temp[index] = 0
            que.append((index + 1, temp))

    return result


def solution(n, info):
    result = bfs(n, info)

    if result:
        return result[-1]
    else:
        return [-1]


print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
