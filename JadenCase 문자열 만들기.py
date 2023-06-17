def solution(s):
    original = s
    s = s.split()
    for i, string in enumerate(s):
        if string[0].isalpha():
            front = s[i][0].upper()
            back = s[i][1:].lower()
            s[i] = front + back
        else:
            s[i] = s[i].lower()

    blank = []
    cnt = 0
    for i in range(len(original)):
        if original[i] == " ":
            cnt += 1
        else:
            if cnt != 0:
                blank.append(cnt)
                cnt = 0
    if cnt:
        blank.append(cnt)
    else:
        blank.append(0)
    result = ""

    for b_num, string in zip(blank, s):
        result += string + (" " * b_num)
    return result
