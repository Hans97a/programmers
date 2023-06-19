def solution(progresses, speeds):
    answer = []

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        if progresses[0] >= 100:
            cnt = 0
            while progresses and progresses[0] >= 100:
                cnt += 1
                del progresses[0]
                del speeds[0]
            answer.append(cnt)

    return answer
