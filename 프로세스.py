def solution(priorities, location):
    cnt = 0

    while priorities:
        top_priority = max(priorities)
        top_priority_idx = priorities.index(top_priority)

        process = priorities.pop(0)
        if process == top_priority and top_priority_idx == 0:
            cnt += 1
            if location == 0:
                return cnt
        else:
            priorities.append(process)
        location = len(priorities) - 1 if location == 0 else location - 1
