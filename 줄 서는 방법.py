"""
dfs -> 시간초과
"""

# answer = []
# arr = []
# def dfs(n, k):
#     global arr, answer

#     if len(arr) == n:
#         answer.append(arr.copy())
#         return

#     for i in range(n):
#         if i + 1 not in arr:
#             arr.append(i+1)
#             dfs(n,k)
#             arr.pop()


# def solution(n, k):
#     global answer
#     dfs(n, k)
#     return answer[k-1]


def solution(n, k):
    people = [i for i in range(1, n + 1)]
    answer = []
    facto = [1, 1]

    for i in range(2, n + 1):
        facto.append(facto[i - 1] * i)

    k -= 1

    while n:
        tmp = facto[n - 1]
        answer.append(people[k // tmp])
        people.pop(k // tmp)
        k, n = k % tmp, n - 1

    return answer


solution(3, 5)
