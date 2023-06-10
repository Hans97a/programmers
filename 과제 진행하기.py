def solution(plans):
    answer = []
    wait_list = []

    for idx, plan in enumerate(plans):
        h, m = map(int, plan[1].split(":"))
        plans[idx][1] = h * 60 + m
        plans[idx][2] = int(plans[idx][2])
    plans.sort(key=lambda x: x[1])

    for subject, start, remaining in plans:
        if wait_list:
            prev_subject, prev_start, prev_remaining = wait_list.pop()
            gap = start - prev_start

            if gap < prev_remaining:
                wait_list.append((prev_subject, prev_start, prev_remaining - gap))
            else:
                answer.append(prev_subject)
                gap = gap - prev_remaining

                while wait_list and gap:
                    prev_subject, prev_start, prev_remaining = wait_list.pop()
                    if gap < prev_remaining:
                        wait_list.append(
                            (prev_subject, prev_start, prev_remaining - gap)
                        )
                        break
                    else:
                        answer.append(prev_subject)
                        gap = gap - prev_remaining

        wait_list.append((subject, start, remaining))

    answer.extend([name for name, _, _ in wait_list[::-1]])

    return answer
