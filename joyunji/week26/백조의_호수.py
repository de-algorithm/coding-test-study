import sys
from collections import deque
input = sys.stdin.readline

dx = (0,0,1,-1)
dy = (1,-1,0,0)

# 두 백조가 만나는지 확인하는 함수 
def bfs():
    next_queue = deque() 
    while swan_queue:
        x, y = swan_queue.popleft()
        if x == swan[1][0] and y == swan[1][1]:
            return True, None
        
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < R and 0 <= ny < C:
                if visited[nx][ny]: continue 
                if lake[nx][ny] != 'X': # 물이라면 계속 이동을 위해 큐에 삽입
                    swan_queue.append((nx,ny))
                else: # 빙판이라면 나중에 물을 녹인 후 확인할 큐에 삽입 
                    next_queue.append((nx,ny))
                visited[nx][ny] = 1
                    
    return False, next_queue


def melt():
    next_water = deque()
    while water:
        x, y = water.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < R and 0 <= ny < C:
                if lake[nx][ny] == 'X':
                    next_water.append((nx,ny))
                    lake[nx][ny] = '.'
            
    return next_water                
    
R, C = map(int, input().split())
lake = []
swan = []
water = deque()

# 데이터 입력 
for i in range(R):
    temp = input().strip()
    for j in range(C):
        if temp[j] == '.' or temp[j] == 'L':
            water.append((i,j))
        if temp[j] == 'L':
            swan.append((i,j))
    lake.append(list(temp))


answer = 0
visited = [[0]*C for _ in range(R)]
swan_queue = deque()

x, y = swan[0][0],swan[0][1]
swan_queue.append((x,y))
visited[x][y] = 1

while True:
    found, next_queue = bfs()
    if found:
        break
    answer += 1
    water = melt()
    swan_queue = next_queue
        

print(answer)