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
    queue = [(0, 0, k)]
    heapq.heapify(queue)
    visited = []
    path = [-1 for _ in range(n)]
    #def traverse_graph(node, time=0, lv=0):
    #    if node not in visited:
    #        visited.append(node)
    #        neighbors = node_dict.get(node, dict())
    #        print(lv, node, neighbors)
    #        for k, v in neighbors.items():
                #traverse_graph(k, time+v, lv+1)
    #traverse_graph(k)
    while queue:
        (lv, weight, node) = heapq.heappop(queue)
        if node not in visited:
            visited.append(node)
            neighbors = node_dict.get(node, dict())
            for key, val in neighbors.items():
                heapq.heappush(queue, (lv+1, val, key))
        print(node, queue)
    return weight
