"""
dfs로 모든 경우의 수를 찾아 최솟값을 찾도록 했으나 테스트 케이스 외 제출 케이스에서 시간 초과 발생

참고 https://velog.io/@injoon2019/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B5%9C%EC%86%9F%EA%B0%92-%EB%A7%8C%EB%93%A4%EA%B8%B0

"""


def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    result = 0
    for a, b in zip(A, B):
        result += a * b
    return result
