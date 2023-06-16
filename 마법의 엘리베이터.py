def solution(storey):
    answer = 0

    while storey >= 1:
        modular = storey % 10

        if modular > 5:
            add = 10 - modular
            storey += add
            answer += add
        elif modular < 5:
            storey -= modular
            answer += modular
        else:
            temp = storey // 10
            if temp % 10 >= 5:
                answer += 10 - modular
                storey += 10 - modular
            else:
                answer += modular
                storey -= modular
        storey //= 10

    return answer


solution(2554)
