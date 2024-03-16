from collections import deque

def solution(m, n, k, coords):
    global graph
    graph = [[1 for j in range(n)] for i in range(m)]
    answer = []

    for x1, y1, x2, y2 in coords:
        for _y in range(y1, y2):
            for _x in range(x1, x2):
                graph[_y][_x] = 0
    
    for _x in range(n):
        for _y in range(m):
            if graph[_y][_x] == 1:
                size = bfs_search(_x, _y, n, m)
                answer.append(size)
    
    answer.sort()
    return answer


def bfs_search(s_x, s_y, n, m):
    queue = deque()
    queue.append((s_x, s_y))
    graph[s_y][s_x] = 0
    count = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for n_x, n_y in map(lambda _dx, _dy: (x+_dx, y+_dy), dx, dy):
            if 0 <= n_x < n and 0 <= n_y < m and graph[n_y][n_x] == 1:
                graph[n_y][n_x] = 0
                count += 1
                queue.append((n_x, n_y))
    return count

m, n, k = list(map(int,input().split()))
coordinates = []
for _ in range(k):
    coordinates.append(list(map(int,input().split())))
result = solution(m, n, k, coordinates)
print(len(result))
print(*result)