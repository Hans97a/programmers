from heapq import heappop, heappush


def solution(n, k, enemy):
    answer, sumEnemy = 0, 0
    heap = []

    for e in enemy:
        heappush(heap, -e)
        sumEnemy += e
        if sumEnemy > n:
            if k == 0:
                break
            sumEnemy += heappop(heap)
            k -= 1
        answer += 1
    return answer


solution(7, 3, [4, 2, 4, 5, 3, 3, 1])
