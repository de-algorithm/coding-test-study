from collections import deque


def solution(N, M, classroom):
    global visit, target
    start_r, start_c = 0, 0
    target = []
    visit = [[[[0]*M for _ in range(N)] for _ in range(4)] for _ in range(4)]
    for i, row in enumerate(classroom):
        for j, each in enumerate(row):
            if each == "S":
                start_r, start_c = i, j
                classroom[start_r][start_c] = "."
            elif each == "C":
                target.append([i, j])
    
    return bfs_search(start_r, start_c, classroom)


def bfs_search(x, y, classroom):
    global visit
    queue = deque([[x, y, 0, 4, 0]]) # count, direction, time
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        r, c, cnt, d, time = queue.popleft()
        if cnt == 3:
            return time
        for comp_d in range(4):
            if comp_d == d: 
                continue
            n_r, n_c = r + dx[comp_d], c + dy[comp_d]
            if not(0 <= n_r < len(classroom) and 0 <= n_c < len(classroom[0])): 
                continue
            if not visit[comp_d][cnt][n_r][n_c]:
                if classroom[n_r][n_c] == "#":
                    continue
                elif classroom[n_r][n_c] == "C":
                    bit = target.index([n_r, n_c])
                    visit[comp_d][cnt | (bit + 1)][n_r][n_c] = 1
                    queue.append([n_r, n_c, cnt | (bit + 1), comp_d, time+1])
                else:
                    visit[comp_d][cnt][n_r][n_c] = 1
                    queue.append([n_r, n_c, cnt, comp_d, time+1])
    return -1

n, m = list(map(int,input().split()))
class_map = [list(input()) for _ in range(n)]
result = solution(n, m, class_map)
print(result)