from collections import deque

def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    r, c = len(maps), len(maps[0])
    visited = [[0]*c for _ in range(r)]
    
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
        
    while q:
        x, y = q.popleft()
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
                
            if 0 <= nx < r and 0 <= ny < c:
                if maps[nx][ny] != 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
        
    return visited[r-1][c-1] if visited[r-1][c-1] != 0 else -1 