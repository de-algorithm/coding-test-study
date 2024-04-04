import sys
from collections import deque
input = sys.stdin.readline

M,N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]
    
answer = []

# 직사각형 영역 방문 체크 상태로 만들기
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] += 1


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    cnt = 1
    
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = 1
                    queue.append((ny, nx))
                    cnt += 1
    return cnt

            
for i in range(M):  
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] += 1
            answer.append(bfs(i,j))

print(len(answer))
print(*sorted(answer))