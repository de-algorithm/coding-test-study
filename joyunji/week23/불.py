# problem: https://www.acmicpc.net/problem/4179

import sys
from collections import deque
input = sys.stdin.readline
R, C = map(int, input().split())
maze = []
for _ in range(R):
    maze.append(list(input().strip()))

# 상,하,좌,우
dx = (1,-1,0,0)
dy = (0,0,1,-1)
def solution(R, C, maze):
    
    q = deque()
    fire = []
    visited = [[False for _ in range(C)] for _ in range(R)]  
    time = 0
    # J(지훈이 초기위치)와 F(불이 난 공간) 찾기
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'J':
                q.append((i,j,0))
                visited[i][j] = True
            elif maze[i][j] == 'F':
                fire.append((i,j))
    
    # 매분마다
    while True:
        if q:
            x, y, t = q.popleft()
            t += 1
            # 현재 위치가 미로의 가장자리라면 탈출 
            if (x == 0 or x == R-1) or (y == 0 or y == C-1):
                break 
        else:
            print_maze()
            break
        
        # 인접한 공간을 지나갈 수 있는지 확인
        print(x, y, t)
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            print(nx, ny)
            # 지훈이는 지나갈 수 있는 공간을 큐에 삽입
            if (0 <= nx < R) and (0 <= ny < C) and (maze[nx][ny] == '.') and (visited[nx][ny] == False):
                q.append((nx,ny,t))
                maze[x][y] = '.'
                maze[nx][ny] = 'J'
                visited[nx][ny] = True
                print("J이동")
        print(q)
        move_fire(fire, maze)
        print_maze()
    
    return t

def move_fire(fire, maze):
    for f in fire:
        fire_x, fire_y = f
        for k in range(4):
            nx, ny = fire_x+dx[k], fire_y+dy[k]
            if (0 <= nx < R) and (0 <= ny < C) and (maze[nx][ny] != '#'):
                maze[nx][ny] = 'F'
            # J를 만나면 q에 있는 해당 위치의 J 삭제  
        
def print_maze():
    for li in maze:
        print(li)
print(solution(R, C, maze)) 