#백준 테크로미노
def solution(n, m, board):
    global sum_max, paper
    sum_max = 0
    paper = board
    for i in range(n):
        for j in range(m):
            find_loc_sum(i, j, board[i][j], [(i,j)])
            find_loc_sum_exc(i, j, board[i][j])
    return sum_max


def find_loc_sum(r, c, s, track):
    global sum_max
    if len(track) == 4:
        sum_max = max(sum_max, s)
        return
    # 4가지 모양 처리 가능
    for dx, dy in  [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        nx, ny = c + dx, r + dy
        if not (0 <= nx < len(paper[0]) and 0 <= ny < len(paper)): continue
        if (ny, nx) not in track:
            find_loc_sum(ny, nx, s + paper[ny][nx], [(ny, nx)]+track)


def find_loc_sum_exc(r, c, s):
    global sum_max
    w_ud, w_lr = [], []
    for d in [-1, 1]:
        if (0 <= c + d < len(paper[0])):
            w_ud.append(paper[r][c+d])
        if 0 <= r + d < len(paper):
            w_lr.append(paper[r+d][c])
    if len(w_ud) >= 2 and len(w_lr) >= 1:
        sum_max = max(sum_max, s+sum(w_ud)+max(w_lr))
    if len(w_lr) >= 2 and len(w_ud) >= 1:
        sum_max = max(sum_max, s+sum(w_lr)+max(w_ud))


n, m = list(map(int, input().split()))
maps = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, m, maps))
