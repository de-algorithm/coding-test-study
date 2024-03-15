from collections import deque
from copy import deepcopy


def solution(N, M, maps):
    global area, max_zero_area
    area = maps
    max_zero_area = 0
    make_wall(0)
    return max_zero_area


def bfs():
    global max_zero_area
    queue = deque()
    copy_area = deepcopy(area)
    dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
    n, m = len(copy_area), len(copy_area[0])
    for i in range(n):
        for j in range(m):
            if copy_area[i][j] == 2:
                queue.append((i,j))
    
    while queue:
        r, c = queue.popleft()
        for d in range(4):
            n_r, n_c = r+dx[d], c+dy[d]
            if 0 <= n_r < n and 0 <= n_c < m and copy_area[n_r][n_c] == 0:
                copy_area[n_r][n_c] = 2
                queue.append((n_r, n_c))
    
    cnt_zero = sum(row.count(0) for row in copy_area)
    max_zero_area = max(max_zero_area, cnt_zero)


def make_wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(len(area)):
        for j in range(len(area[0])):
            if area[i][j] == 0:
                area[i][j] = 1
                make_wall(cnt + 1)
                area[i][j] = 0
