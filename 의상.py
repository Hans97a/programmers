def solution(clothes):
    dict = {cloth[1]: [] for cloth in clothes}
    for cloth, cloth_type in clothes:
        dict[cloth_type].append(cloth)

    result = 1

    arr = []
    for cloth_type, kleidungen in dict.items():
        arr.append(len(kleidungen) + 1)
    for num in arr:
        result *= num

    return result - 1
