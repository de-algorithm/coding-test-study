# 백준 연구소3
from collections import deque
from itertools import combinations

def solution(n: int, m: int, maps:list[list[int]]) -> int:
    global area
    area = maps
    viruses = []
    min_activate_time = float('inf')
    for i in range(n):
        for j in range(n):
            if area[i][j] == 2:
                viruses.append((i, j))
    viruses = list(combinations(viruses, m))
    for exp_virus in viruses:
        min_activate_time = min(move_virus(n, exp_virus), min_activate_time) 
    
    if min_activate_time == float('inf'):
        return -1
    return min_activate_time


def move_virus(n, virus):
    local_max_time = 0
    queue = deque()
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]

    for v_i, v_j in virus:
        queue.append((v_i,v_j))
        visited[v_i][v_j] = 0
    
    while queue:
        curr_i, curr_j = queue.popleft()

        for d in range(4):
            next_i = curr_i + dx[d]
            next_j = curr_j + dy[d]
            if not (0 <= next_i < n and 0 <= next_j < n): continue
            if area[next_i][next_j] == 1: continue
            if visited[next_i][next_j] == -1:
                visited[next_i][next_j] = visited[curr_i][curr_j] + 1
                queue.append((next_i, next_j))
                if area[next_i][next_j] == 0:
                    local_max_time = max(local_max_time, visited[next_i][next_j])

    for i in range(n):
        for j in range(n):
            if area[i][j] == 0 and visited[i][j] == -1:
                return float('inf')
    return local_max_time


n, m = list(map(int,input().split()))
lab_map = []
for _ in range(n):
    lab_map.append(list(map(int,input().split())))
print(solution(n, m, lab_map))