import sys 
from collections import defaultdict
import heapq

def dijkstra_q(start, graph, N):
    distance = [INF] * (N+1)
    distance[start] = 0
    
    q = []
    heapq.heappush(q, (0, start))   # 시작노드 (걸린시간, 정점)을 우선순위 큐에 삽입

    while q:
        dist, node = heapq.heappop(q)
        # 큐에서 뽑은 노드의 시간이 이미 갱신된 시간보다 클 경우 무시
        if distance[node] < dist:
            continue
        
        # 큐에서 뽑은 노드와 연결된 인접 노드들 탐색
        for next in graph[node]:
            cost = distance[node] + next[1]     
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
    return distance

sys.stdin = open("yunji/input.txt", "r")
INF = int(1e9)
N, M, X = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(M):
    start, end, t = map(int, sys.stdin.readline().split())
    graph[start].append([end, t])   # 단방향 

min_to_X = []    # 학생들이 X번 마을로 가는 최단거리 리스트
# 학생들이 X번 마을로 가는 최단 경로 구하기 
for i in range(1, N+1):
    if i==X:
        min_to_X.append(0)
    else:
        min_to_X.append(dijkstra_q(i, graph, N)[X])

min_to_home = dijkstra_q(X, graph, N)[1:] # 학생들이 집으로 돌아가는 최단거리 리스트

# 학생들이 X번 마을로 가는 최단 거리 + 학생들이 집으로 돌아가는 최단거리 
answer = max([x + y for x, y in zip(min_to_X, min_to_home)])
print(answer)
    

