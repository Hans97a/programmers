def solution(s):
    answer = 9999
    if len(s) == 1:
        return 1

    for i in range(1, len(s)):
        cnt = 1
        char = s[:i]
        string = ""

        for j in range(i, len(s), i):
            compare = s[j : i + j]
            if char == compare:
                cnt += 1
            else:
                if cnt != 1:
                    string += f"{cnt}{char}"
                else:
                    string += f"{char}"
                char = compare
                cnt = 1

        if cnt != 1:
            string += f"{cnt}{char}"
        else:
            string += f"{char}"
        answer = min(answer, len(string))

    return answer
