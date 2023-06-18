def solution(want, number, discount):
    answer = 0
    want_dic = {item: number[i] for i, item in enumerate(want)}

    for i in range(len(discount)):
        arr = discount[i : i + 10]
        check = True
        for w, n in want_dic.items():
            if arr.count(w) != n:
                check = False
                break
        if check:
            answer += 1

    return answer
