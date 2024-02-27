import sys
from collections import defaultdict
import heapq
sys.stdin = open("yunji/input.txt", "r")


def dijkstra(graph, time, c):
    q = []
    heapq.heappush(q, (0, c))   # 시작노드 (걸린시간, 정점)을 우선순위 큐에 삽입
    time[c] = 0                 
    
    while q:
        t, node = heapq.heappop(q)
        # 큐에서 뽑은 노드의 시간이 이미 갱신된 시간보다 클 경우 무시
        if time[node] < t:
            continue
        
        # 큐에서 뽑은 노드와 연결된 인접 노드들 탐색
        for next in graph[node]:
            cost = time[node] + next[1]     
            if cost < time[next[0]]:
                time[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
                
    count = 0
    total_time = 0
    for val in time[1:]:
        if val is not INF:
            count +=1
            if total_time < val:
                total_time = val
                
    return count, total_time
    
T = int(sys.stdin.readline())
INF = int(1e9)
for i in range(T):
    n, d, c = map(int, sys.stdin.readline().split())
    
    graph = defaultdict(list)
    visited = [False] * (n+1)
    time = [INF] * (n+1)
    
    for j in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b].append([a, s])
        
    count, total_time = dijkstra(graph, time, visited, c)
    print(count, total_time)
    