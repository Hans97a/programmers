result = {}
alphabets = "AEIOU"
word = ""
cnt = 1
length = 1


def dfs():
    global word, result, cnt, length
    if len(word) == length:
        try:
            result[word]
            return
        except:
            result[word] = cnt
            cnt += 1
            length += 1

    if length <= 5:
        for i in range(5):
            word += alphabets[i]
            dfs()
            length -= 1
            word = word[:-1]


def solution(word):
    global result
    dfs()
    return result[word]


solution("EIO")
