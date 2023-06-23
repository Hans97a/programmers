def solution(record):
    answer = []

    userlist = {}
    indexlist = {}
    idx = 0
    for rec in record:
        rec = rec.split()
        if rec[0] == "Enter":
            userlist[rec[1]] = rec[2]
            answer.append("님이 들어왔습니다.")
            if rec[1] in indexlist:
                indexlist[rec[1]].append(idx)
            else:
                indexlist[rec[1]] = [idx]
            idx += 1
        elif rec[0] == "Leave":
            answer.append("님이 나갔습니다.")
            if rec[1] in indexlist:
                indexlist[rec[1]].append(idx)
            else:
                indexlist[rec[1]] = [idx]
            idx += 1
        else:
            userlist[rec[1]] = rec[2]

    for userid, arr in indexlist.items():
        for i in arr:
            answer[i] = userlist[userid] + answer[i]
    return answer
