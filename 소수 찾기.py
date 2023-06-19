from itertools import permutations


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    numbers = list(numbers)
    answer = 0
    set_nums = set()
    for i in range(len(numbers)):
        permutation = permutations(numbers, i + 1)
        for perm in permutation:
            num = int("".join(perm))
            set_nums.add(num)
    for num in set_nums:
        if is_prime(num):
            answer += 1

    return answer
