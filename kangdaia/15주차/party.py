from collections import defaultdict
from heapq import heappop, heappush


def visit_party(N: int, M: int, X: int, roads: list[str]) -> int:
    """
    각 노드에서 X까지 도착할 때의 최솟값을 구해서 비교해야 함.

    Args:
        N (int): N개의 마을 (각 마을마다 학생 출발)
        M (int): M개의 길
        X (int): 파티 위치 (도착지)
        roads (list[str]): 각 도시를 연결하는 도로와 소요 시간(가중치)

    Returns:
        int: 각 마을에서 X까지 갔다 올 때 걸리는 최대 시간
    """
    graph = dict()
    for road in roads:
        s, e, t = road.split()
        if int(s) not in graph:
            graph[int(s)] = defaultdict(lambda: float("inf"))
        graph[int(s)][int(e)] = int(t)
    
    def find_time_oneway(start):
        visited = defaultdict(lambda: float("inf"))
        heap = []
        heappush(heap, (0, start))
        visited[start] = 0

        while heap:
            t, v = heappop(heap)

            if visited[v] < t:
                continue
            neighbors = graph[v].items() if v in graph else []
            for next_v, next_t in neighbors:
                new_t = next_t + t
                if new_t < visited[next_v]:
                    visited[next_v] = new_t
                    heappush(heap, (new_t, next_v))
        return visited
    
    max_time_roundtrip = 0
    from_x = find_time_oneway(X)
    for each in range(1, N+1):
        from_each = find_time_oneway(each)
        max_time_roundtrip = max(max_time_roundtrip, from_each[X] + from_x[each])

    return max_time_roundtrip


if __name__ == "__main__":
    print("========TEST 1=========")
    line_1 = map(lambda x: int(x), "4 8 2".split())
    road = ["1 2 4",
            "1 3 2",
            "1 4 7",
            "2 1 1",
            "2 3 5",
            "3 1 2",
            "3 4 4",
            "4 2 3"]
    result = visit_party(*line_1, road)
    print(result, result == 10)