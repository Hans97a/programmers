import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K and len(scoville) >= 2:
        minimum = heapq.heappop(scoville)
        next = heapq.heappop(scoville)
        heapq.heappush(scoville, minimum + next * 2)
        answer += 1

    if min(scoville) < K:
        return -1

    return answer
