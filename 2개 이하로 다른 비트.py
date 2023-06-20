def solution(numbers):
    answer = []

    for number in numbers:
        if number % 2 == 0:
            string = list(bin(number)[2:])
            string[-1] = "1"
        else:
            string = bin(number)[2:]
            string = "0" + string
            idx = string.rfind("0")
            string = list(string)
            string[idx] = "1"
            string[idx + 1] = "0"
        result = int("".join(string), 2)
        answer.append(result)

    return answer
