from collections import deque


def solution(order):
    answer = 0
    arr = deque([i + 1 for i in range(len(order))])
    sub_arr = []

    for num in order:
        while arr and arr[0] != num and arr[0] < num:
            sub_arr.append(arr.popleft())

        if arr and arr[0] == num:
            answer += 1
            arr.popleft()
        elif sub_arr and sub_arr[-1] == num:
            answer += 1
            sub_arr.pop()
        else:
            break

    return answer
