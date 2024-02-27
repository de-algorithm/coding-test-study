import sys, heapq

def solution(n, s, a, b, fares):
    INF = sys.maxsize
    
    # 인접 리스트 생성
    graph = [[] for _ in range(n+1)]
    for c,d,f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))
        
    # 다익스트라 구현
    def dijkstra(start):
        distance = [INF] * (n+1)
        distance[start] = 0
        
        q = []
        # 시작 노드로 가기 위한 최단 경로는 0으로 설정항 큐에 삽입
        heapq.heappush(q, (0, start))
        
        while q:
            # 가장 최단 거리인 노드에 대한 정보 꺼내기
            dist, node = heapq.heappop(q)
            # 현재 노드가 이미 처리됐다면 skip
            if distance[node] < dist:
                continue
            
            # 현재 노드와 연결된 다른 인접한 노드 확인
            for next in graph[node]:
                cost = distance[node] + next[1]
                # 현재 노드를 거치면 이동 거리가 더 짧은 경우
                if cost < distance[next[0]]:
                    distance[next[0]] = cost
                    heapq.heappush(q, (cost, next[0]))
        
        return distance
    
    # i번째 노드에서 시작해서 모든 노드로 도착하는 최단 거리를 구함
    D = [0] + [dijkstra(i) for i in range(1, n+1)]
    
    path = INF
    for i in range(1, n+1):
        path = min(path, D[s][i] + D[i][a] + D[i][b])
        
    return path