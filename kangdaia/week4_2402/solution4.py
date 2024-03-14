from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 1
    trucks = deque(truck_weights)
    bridge = deque([0]*(bridge_length-1)) 
    curr_w = trucks.popleft()
    bridge.append(curr_w)
    
    while trucks:
        out_t = bridge.popleft()
        curr_w -= out_t
        if len(bridge) <= bridge_length and trucks[0] + curr_w <= weight:
            next_t = trucks.popleft()
            curr_w += next_t
            bridge.append(next_t)
        else:
            bridge.append(0)
        answer += 1
    return answer + bridge_length