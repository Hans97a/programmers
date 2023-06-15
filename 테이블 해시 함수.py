def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: [x[col - 1], -x[0]])
    arr = []
    for i in range(row_begin - 1, row_end):
        idx = i + 1
        num = 0
        for el in data[i]:
            num += el % idx
        arr.append(num)
    bit_result = 0
    for el in arr:
        bit_result = bit_result ^ el

    return bit_result
