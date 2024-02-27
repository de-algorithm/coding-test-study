
def solution(N, road, K):
    # graph 생성
    graph = [[] for _ in range(N+1)]
    for a,b,c in road:
        graph[a].append([b,c])
        graph[b].append([a,c])
        
    # 방문여부 리스트
    visited = [False] * (N+1)

    # 최단거리 테이블을 모두 무한으로 초기화
    INF = int(1e9) # 무한 (10억)
    distance = [INF] * (N+1)    
    
    # 방문하지 않은 노드 중에서 최단 거리가 짧은 노드번호 반환
    def get_smallest_node():
        min_val = INF
        idx = 0 # 노드 번호
        for i in range(1, N+1):
            if distance[i] < min_val and not visited[i]:
                min_val = distance[i]
                idx = i
        return idx
    
    def dijkstra(start):
        visited[start] = True
        distance[start] = 0
        
        for j in graph[start]: # j: [연결된 마을번호, 걸리는 시간]            
            if distance[j[0]] > j[1]:    # 무한대 > j[1] 경우와 이미 값이 있을 때 더 짧은 경로로 갱신
                distance[j[0]] = j[1]
    
        # 시작 노드를 제외한 전체 n-1개의 노드에 대한 반복
        for i in range(N-1):
            # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
            now = get_smallest_node()
            visited[now] = True
            
            # 현재 노드와 연결된 다른 노드 확인
            for j in graph[now]:
                cost = distance[now] + j[1]
                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[j[0]]:
                    distance[j[0]] = cost
    
    dijkstra(1) # 1번 마을 
    print(distance)
    answer = len([x for x in distance if x <= K])
    return answer