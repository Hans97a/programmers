def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = [[t_weight, bridge_length] for t_weight in truck_weights]
    on_bridge = []

    while len(trucks) != 0 or len(on_bridge) != 0:
        answer += 1
        bridge_weight = 0
        to_delete = []
        for idx, truck in enumerate(on_bridge):
            if truck[1] <= 1:
                to_delete.append(idx)
            else:
                bridge_weight += truck[0]
                on_bridge[idx][1] -= 1

        on_bridge = [on_bridge[i] for i in range(len(on_bridge)) if not i in to_delete]

        if trucks and bridge_weight + trucks[0][0] <= weight:
            on_bridge.append(trucks.pop(0))
            # on_bridge[len(on_bridge)-1][1] -= 1

    return answer
