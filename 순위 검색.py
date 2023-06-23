to_database_key = {
    "java": "1",
    "python": "2",
    "cpp": "3",
    "backend": "1",
    "frontend": "2",
    "junior": "1",
    "senior": "2",
    "pizza": "1",
    "chicken": "2",
    "-": "-",
}


def keyCheck(key, query_arr):
    global to_database_key
    key_lang, key_job, key_career, key_food = list(key)
    language, job, career, food, score = query_arr

    if to_database_key[language] in [key_lang, "-"]:
        if to_database_key[job] in [key_job, "-"]:
            if to_database_key[career] in [key_career, "-"]:
                if to_database_key[food] in [key_food, "-"]:
                    return True
    return False


def binary_search(list, target, start, end):
    if start >= end:
        return start
    mid = (start + end) // 2
    if list[mid] >= target:
        return binary_search(list, target, start, mid)
    else:
        return binary_search(list, target, mid + 1, end)


def solution(info, query):
    answer = []
    database = {}

    for detail in info:
        detail_arr = detail.split(" ")
        language, job, career, food, score = detail_arr
        if language == "java":
            language = "1"
        elif language == "python":
            language = "2"
        else:
            language = "3"
        job = "1" if job == "backend" else "2"
        career = "1" if career == "junior" else "2"
        food = "1" if food == "pizza" else "2"
        database_key = language + job + career + food
        try:
            database[database_key].append(int(score))
        except Exception:
            database[database_key] = [int(score)]

    for key in database.keys():
        database[key].sort()

    for query_detail in query:
        detail_arr = query_detail.split(" and ")
        food, score = detail_arr[-1].split()
        language, job, career = detail_arr[0], detail_arr[1], detail_arr[2]

        cnt = 0
        for key, scores in database.items():
            if keyCheck(key, [language, job, career, food, int(score)]):
                score = int(score)
                cnt += len(scores) - binary_search(scores, score, 0, len(scores))

        answer.append(cnt)

    return answer
