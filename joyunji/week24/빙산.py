import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

answer = 0
def bfs(i, j):
    global iceberg_count 
    iceberg_count += 1
    q = deque()
    q.append((i,j))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if iceberg[nx][ny] > 0 and visited[nx][ny] == 0: # 얼음이며 방문한 적 없으면 
                    q.append((nx, ny))
                    visited[nx][ny] = iceberg_count # 해당 칸에 빙산 덩어리 번호 부여


temp = [[0 for _ in range(M)] for _ in range(N)] # 빙산의 각각 녹일 높이 
time = 0

while True:
    time += 1 
    ice_count = 0 # 남아있는 얼음 개수 
    iceberg_count = 0 # 빙산 덩어리 번호 

    # 인접한 칸들의 바다 수 확인
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] > 0: # 빙산이라면 인접한 칸들의 바다 수 확인 
                ice_count += 1
                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if iceberg[nx][ny] == 0: # 인접한 칸이 바다라면 
                            temp[i][j] += 1 # 녹일 높이 증가  
    
    # 빙산이 분리되지 않고 모두 녹았을 때 
    if ice_count == 0:
        break
    
    # 빙산 녹이기
    for i in range(N):
        for j in range(M):
            iceberg[i][j] -= temp[i][j]
            if iceberg[i][j] < 0:
                iceberg[i][j] = 0
            temp[i][j] = 0 # 초기화 
    
    visited =  [[0 for _ in range(M)] for i in range(N)]
    # 덩어리 개수 구하기
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] > 0 and visited[i][j] == 0: # 얼음이며 방문한 적 없으면
                bfs(i, j)
    
    # 덩어리가 2개 이상일 때 
    if iceberg_count > 1:
        answer = time
        break
    
print(answer)



