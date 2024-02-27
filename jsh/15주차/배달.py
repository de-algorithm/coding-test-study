"""
N : 마을의 개수
road : 도로 정보 ( a <-> b 간 c의 시간이 필요)
K : 시간

#1. 일단 이어지는 노드를 넣을 dict 하나 선언 ( dist )
#2. 각 마을별 최소값을 넣을 리스트 ( visit_cost )
#3. 1번마을부터 비교
    비교조건 1. K 시간 이하
    비교조건 2. 기존 최소값과 비교해서 더 작을 경우만 갱신
"""
from collections import defaultdict, deque

def solution(N, road, K):
    
    # 1.일단 이어지는 노드를 넣을 dict 하나 선언 ( dist )
    dist = defaultdict(list)
    for a, b, c in road:
        dist[a].append((b,c))
        dist[b].append((a,c))

    #2. 각 마을별 최소값을 넣을 리스트 ( visit_cost )
    # K는 음식 배달이 가능한 시간을 나타내며, 1 이상 500,000 이하 이므로
    # 5000001로 선언
    visit_cost = [500001 for _ in range(N+1)]
    visit_cost[1] = 1
    
    # 앞으로 비교할 데이터 저장 deque
    deq = deque([(1, 0)])
    
    while deq:
        node, time = deq.popleft()
        
        # 인접한 노드들중 시간이 K보다 작거나 같고, 
        # 방문했더라도 현재 걸린 시간이 기록된 시간보다 짧으면 
        for v, w in dist[node]:
            if time + w <= K and time + w <= visit_cost[v]:
                # 다음 비교를 하기위해 deque에 저장
                deq.append((v, time + w))
                # 최소값 최신화
                visit_cost[v] = time + w
        
    answer = N+1-visit_cost.count(500001)

    return answer