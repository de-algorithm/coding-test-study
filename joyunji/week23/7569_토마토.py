import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
tomatoes = []
q = deque()
visited = [[[0]*M for _ in range(N)]for _ in range(H)]
zero_count = 0
rippen_count = 0
day = 0
answer = 0
for i in range(H):
    temp = []
    for j in range(N):
        line = list(map(int, input().split()))
        for k in range(M):
            if line[k] == 0:
                zero_count += 1
            elif line[k] == 1:
                q.append((i,j,k,day))
                visited[i][j][k] = 1
        temp.append(line)
    tomatoes.append(temp)

# 동,서,남,북,위,아래
move = [(1,0,0), (-1,0,0), (0,-1,0), (0,1,0), (0,0,1), (0,0,-1)]

while q:
    z, y, x, d = q.popleft()
    # 상우하좌 4 방향 탐색
    for k in range(6):
        # 상우하좌 위치 이동한 좌표값 
        nx, ny, nz = x+move[k][0], y+move[k][1], z+move[k][2]
        # 좌표값이 박스 내에 존재하고, 안익은 토마토이며, 방문한 적이 없다면 
        if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
            if tomatoes[nz][ny][nx] == 0 and visited[nz][ny][nx] == 0:
            # 방문 처리 및 이동거리 누적 
                visited[nz][ny][nx] = 1
                tomatoes[nz][ny][nx] = 1
                rippen_count += 1
                # 큐에 삽입
                q.append((nz,ny,nx, d+1)) 
                answer = d+1
# 모든 토마토가 익은 경우
if zero_count == rippen_count:
    print(answer)
# 익지 않은 토마토가 있는 경우
elif zero_count > rippen_count:
    print(-1)