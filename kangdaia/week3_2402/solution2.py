from heapq import heappush, heappop
from collections import defaultdict


def solution(n: int, s: int, a: int, b: int, fares: list[list[int]]) -> int:
    """_summary_

    Args:
        n (int): _description_
        s (int): _description_
        a (int): _description_
        b (int): _description_
        fares (list[list[int]]): _description_

    Returns:
        int: _description_
    """
    graph = dict()
    for loc1, loc2, weight in fares:
        if loc1 not in graph:
            graph[loc1] = defaultdict(int)
        if loc2 not in graph:
            graph[loc2] = defaultdict(int)
        graph[loc1][loc2] = weight
        graph[loc2][loc1] = weight

    def find_path(start_node):
        queue = []
        dist = defaultdict(lambda: float("inf"))

        heappush(queue, (0, start_node))
        dist[start_node] = 0

        while queue:
            w, c = heappop(queue)

            if dist[c] < w:
                continue
            if c not in graph:
                continue
            for k, v in graph[c].items():
                next_w = v + w
                if next_w < dist[k]:
                    heappush(queue, (next_w, k))
                    dist[k] = next_w
        return dist

    from_start = find_path(s)
    min_fares = float("inf")

    for node in range(1, n + 1):
        if node == s:
            continue
        dist_node = find_path(node)
        min_fares = min(min_fares, from_start[node] + dist_node[a] + dist_node[b])

    return min(from_start[a] + from_start[b], min_fares)
