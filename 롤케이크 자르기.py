def solution(topping):
    answer = 0

    chulsoo = {}
    brother = {}

    for num in topping:
        try:
            chulsoo[num] += 1
        except:
            chulsoo[num] = 1

    for num in topping:
        try:
            brother[num] += 1
        except:
            brother[num] = 1

        chulsoo[num] -= 1
        if chulsoo[num] <= 0:
            del chulsoo[num]

        if len(chulsoo) == len(brother):
            answer += 1

    return answer
