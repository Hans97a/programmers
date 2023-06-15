def solution(n):
    b_cnt = bin(n).count("1")

    while True:
        n += 1
        cnt = bin(n).count("1")
        if cnt == b_cnt:
            return n
