# problem: https://www.acmicpc.net/problem/6593

# 각 층 사이에 빈줄이 있음
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    # 동,서,남,북,위,아래
    move = [(1,0,0), (-1,0,0), (0,-1,0), (0,1,0), (0,0,1), (0,0,-1)]
    
    while q:
        z,x,y,t = q.popleft()
        if building[z][x][y] == 'E':
            return f"Escaped in {t} minute(s)."
        for k in range(6):
            nx, ny, nz = x+move[k][0], y+move[k][1], z+move[k][2]
            
            if 0<= nx < R and 0 <= ny < C and 0 <= nz < L:
                if not visited[nz][nx][ny] and building[nz][nx][ny] != '#':
                    visited[nz][nx][ny] = t+1
                    q.append((nz,nx, ny,t+1))
    else:
        return "Trapped!" 

answer = []
while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    q = deque()
    visited = [[[0]*C for _ in range(R)]for _ in range(L)] 
    building = []
    for i in range(L):
        floor = []
        for j in range(R+1):
            temp = list(input().strip())
            if not temp:
                continue
            for k in range(C):
                if temp[k] == 'S':
                    q.append((i,j,k,0)) # 층, 행, 열, 시간 
                    visited[i][j][k] = 1
            floor.append(temp)
        building.append(floor)
    answer.append(bfs())

for item in answer:
    print(item)
    