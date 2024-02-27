from heapq import heappop, heappush

def village_order(N: int, road: list[list[int]], K: int) -> int:
    """다익스트라 알고리즘
    - 도착 노드 대신 시간 (거리 가중치)가 정해져 있는 경우

    1. graph 노드 가중치 data type 바꾸기
        - graph (list[list[int]]), 간선이 없는 곳은 가중치 float("inf")
        - 중복 간선 존재하기 때문에 min을 통해 가중치가 가장 작은 값으로 적용
    2. dist 목록 initialization to float("inf")
    3. dist[1] = 0; 노드 1 거리(시간) 0
    4. heap에 거리 0 인 노드 1 push

    5. heap이 빌 때 까지,
        - heap pop
        - 현재 최소 거리를 가진 노드가 이미 최소 값을 가지고 있거나,
            조건인 시간을 넘어갔으면 -> PASS
        - 인접 노드 목록에서
            - 새로운 가중치를 계산해, dist 목록에 있는 값보다 최소 값이면,
                dist 갱신 및 새로운 가중치로 heap push
    6. 계산한 dist 값에서 가충치가 K값 이하인 경우를 count

    Args:
        N (int): 노드의 갯수
        road (list[list[int]]): 노드가 연결되어 있는 정보와 가중치
        K (int): 가중치의 최대값

    Returns:
        int: 가중치의 최대값을 넘지 않는 노드의 갯수
    """
    graph = [[float("inf") for _ in range(N+1)] for _ in range(N+1)]
    for start_n, end_n, w in road:
        graph[start_n][end_n] = min(graph[start_n][end_n], w)
        graph[end_n][start_n] = min(graph[end_n][start_n], w)
    
    dist = [float("inf") for _ in range(N+1)]
    dist[1] = 0
    heap = []

    heappush(heap, (0, 1))

    while heap:
        w, nd = heappop(heap)
        
        if dist[nd] < w or w > K:
            continue
        for next_nd, next_w in enumerate(graph[nd]):
            new_w = next_w + w
            if new_w < dist[next_nd]:
                dist[next_nd] = new_w
                heappush(heap, (new_w, next_nd))

    cnt_village = 0
    for d in dist:
        if d <= K:
            cnt_village += 1
    return cnt_village