from collections import deque
def solution(bridge_length, weight, truck_weights):
    
    dq = deque()
    sum_weight = truck_weights[0] # 현재 다리에 올라간 트럭의 무게 합
    dq.append(truck_weights[0])
    
    time = 1 # 경과 시간 
    i = 1   # truck_weights의 인덱스 

    while i < len(truck_weights):
        time += 1   # 시간 증가
        
        # 다리에 자리가 없을 때
        if len(dq) == bridge_length:
            sum_weight -= dq.popleft() # 다리를 건넌 트럭
    
        # 다리에 자리가 있으며 현재 트럭이 다리에 올라갈 수 있는 무게라면 
        if len(dq) < bridge_length and sum_weight + truck_weights[i] <= weight:
            sum_weight += truck_weights[i]
            dq.append(truck_weights[i])
            i += 1
        
        # 다리에 자리는 있는데 트럭 무게가 초과될 경우
        elif len(dq) < bridge_length and sum_weight + truck_weights[i] > weight:
            dq.append(0)    # 가상의 트럭 
        
    
    return time + bridge_length