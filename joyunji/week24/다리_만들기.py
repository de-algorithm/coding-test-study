import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x, y):
    q = deque()
    q.append((x,y))
    while q:
        x, y= q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if map[nx][ny] == 1 and visited[nx][ny] == 0:  
                    q.append((nx, ny))
                    visited[nx][ny] = island_num

def bfs_sea(x, y):
    q = deque()
    q.append((x,y))
    while q:
        x, y, c = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if map[nx][ny] == 0 and visited_3[nx][ny] == 0:  
                    q.append((nx, ny, c+1))
                    visited_3[nx][ny] = 1
                    
                if map[nx][ny] != 0 and map[nx][ny] != map[x][y]:
                    break

# 섬 번호 매기기
island_num = 0

visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if map[i][j] == 1 and visited[i][j] == 0: 
            island_num += 1
            bfs(i, j)

map = visited
answer = float('inf')
# 섬 가장자리에서 최단거리의 다른 섬 찾기 
for i in range(N):
    for j in range(N):
        visited_2 = [[0 for _ in range(N)] for _ in range(N)]
        if map[i][j] != 0 and visited_2[i][j] == 0: # 섬이고 방문한 적이 없다면 
            for k in range(4): # 인접한 칸에서 
                nx, ny = i+dx[k], j+dy[k]
                if 0 <= nx < N and 0 <= ny < N: 
                    if map[nx][ny] == 0 and visited_2[nx][ny] == 0: # 바다이고 방문한 적이 없다면
                        visited_3 = [[0 for _ in range(N)] for _ in range(N)]
                        answer = min(answer, bfs_sea(nx,ny, 0))
                        
            
print(answer)

            