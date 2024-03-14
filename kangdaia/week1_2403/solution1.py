from collections import deque, defaultdict


def solution(land):
    global graph
    graph = list(map(list, zip(*land)))
    area_sum = defaultdict(int)
    col_sums = [0] * len(graph)
    for each_c in range(len(graph)):
        while 1 in graph[each_c]:
            each_r = graph[each_c].index(1)
            if graph[each_c][each_r] == 1:
                key = chr(ord("a")+each_c)+str(each_r)
                area_sum[key] = bfs(each_r, each_c, key)
    for i in range(len(graph)):
        col_key = set(graph[i])
        convert2area = map(lambda x: area_sum[x], col_key)
        col_sums[i] = sum(convert2area)
    return max(col_sums)


def bfs(r, c, key):
    visited = set()
    queue = deque([(c, r)])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    n, m = len(graph), len(graph[0])
    while queue:
        curr = queue.popleft()
        if curr not in visited:
            visited.add(curr)
            graph[curr[0]][curr[1]] = key
            for d in zip(dx, dy):
                n_c, n_r = curr[0]+d[0], curr[1]+d[1]
                if 0 <= n_r < m and 0 <= n_c < n and graph[n_c][n_r] == 1:
                    queue.append((n_c, n_r))
    return len(visited)
