from collections import deque


def solution(N: int, M: int, classroom: list[str]):
    start_r, start_c = 0, 0
    target = []
    visit = [[[[0]*M for _ in range(N)] for _ in range(4)] for _ in range(4)]
    for i, row in enumerate(classroom):
        row_lst = list(row)
        if "S" in row_lst:
            start_r, start_c = i, row_lst.index("S")
        for j, each in enumerate(row_lst):
            if each == "C":
                target.append([i, j])
    
    return bfs_search(start_c, start_r, visit, classroom, target)

def bfs_search(x, y, visit, classroom, target):
    queue = deque()
    queue.append([y, x, 0, 4, 0]) # count, direction, time
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    time = -1
    while queue:
        r, c, cnt, d, time = queue.popleft()
        if cnt == 3:
            break
        for comp_d in range(4):
            n_c, n_r = c + dx[comp_d], r + dy[comp_d]
            if comp_d == d or classroom[n_r][n_c] == "#": continue
            if not(0 <= n_c < len(classroom[0]) and 0 <= n_r < len(classroom)): continue
            if not visit[comp_d][cnt][r][c]:
                if classroom[n_r][n_c] == "C":
                    bit = target.index([n_r, n_c])
                    cnt = cnt | (bit + 1)
                visit[comp_d][cnt][n_r][n_c] = 1
                queue.append([n_r, n_c, cnt, comp_d, time])
    return time