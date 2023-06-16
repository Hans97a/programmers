def solution(k, tangerine):
    answer = 0
    dic = {}
    for num in tangerine:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    arr = sorted(list(dic.values()), reverse=True)
    i = 0
    while k > 0:
        k -= arr[i]
        i += 1
        answer += 1

    return answer
