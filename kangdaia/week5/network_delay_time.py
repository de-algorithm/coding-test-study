import heapq
def min_time_cost(times: list[list[int]], n: int, k: int) -> int:
    """
    for given times, n, and k,
    calculate the minimum times take to travel all nodes.

    Args:
        times (list[list[int]]): weighted directed graph in 2d-array
        n (int): number of nodes in network. at least 1 node exists.
        k (int): starting node number

    Returns:
        int: minimum times take to travel all nodes.
            return -1 if cannot visit all nodes.
    """
    node_dict = dict()
    for time in times:
        val = node_dict.get(time[0], dict())
        val[time[1]] = time[2]
        node_dict[time[0]] = val
    queue = [(0, k)]
    heapq.heapify(queue)
    path = [float('inf') for _ in range(n)]
    path[k-1] = 0

    while queue:
        (dist, node) = heapq.heappop(queue)
        path[node-1] = min(path[node-1], dist)
        if path[node-1] >= dist:
            neighbors = node_dict.get(node, dict())
            for key, val in neighbors.items():
                if val+dist < path[key-1]:
                    path[key-1] = val+dist
                    heapq.heappush(queue, (val+dist, key))
    return -1 if float('inf') in path else max(path)
