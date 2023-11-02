n, m = map(int, input().split())
r, c, d = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0

while True:
    if ls[r][c] == 0:
        ls[r][c] = -1
        ans += 1
    
    flag = 0
    for _ in range(4):
        nx = r + dx[(d+3) % 4]
        ny = c + dy[(d+3) % 4]
        d = (d+3) % 4

        if 0 <= nx < n and 0 <= ny < m and ls[nx][ny] == 0:
            r, c = nx, ny 
            flag = 1
            break
    
    if flag == 0:
        nx = r - dx[d]
        ny = c - dy[d]

        if 0 <= nx < n and 0 <= ny < m and ls[nx][ny] != 1:
            r, c = nx, ny
        else:
            break

print(ans)
