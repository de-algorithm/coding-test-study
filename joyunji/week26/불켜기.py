import sys
from collections import deque, defaultdict

input = sys.stdin.readline
N, M = map(int, input().split())
barn = [[0]*(N+1) for _ in range(N+1)]
barn[1][1] = 1
switches = defaultdict(list)

for _ in range(M):
    x,y,a,b = map(int, input().split())
    switches[(x,y)].append((a,b))


dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 1
visited = [[0]*(N+1) for _ in range(N+1)]

q = deque()
q.append((1,1))
visited[1][1] = 1

while q:
    x, y = q.popleft() # 현재 방의 위치 x,y
    
    # 방에 있는 스위치로 다른 방의 불을 모두 킴 
    for a, b in switches[(x,y)]:
        if barn[a][b] == 0: # 불이 안 켜져있다면 
            barn[a][b] = 1  # 킴
            cnt += 1        
            
            # 새로 불을 켠 방의 인접한 방을 탐색
            for k in range(4):
                na, nb = a+dx[k], b+dy[k]
                if 1 <= na <= N and 1 <= nb <= N:
                    if visited[na][nb]: # 방문한 적이 있다면 큐 삽입
                        q.append((na, nb)) 
    # 현재 방의 인접한 방 탐색        
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 1 <=nx <= N and 1 <= ny <= N:
            if barn[nx][ny] == 1 and visited[nx][ny]==0: # 불이 켜져 있고 방문한 적 없는 방이라면 
                q.append((nx, ny))
                visited[nx][ny] = 1
    
print(cnt)

'''
2024/05/26

11967. 불켜기

<문제>
- 유일하게 불이 켜져있는 (1, 1)방에서 출발
- 어떤 방에는 다른 방의 불을 끄고 켤 수 있는 스위치가 있음  
- 불이 켜져있는 방으로만 들어갈 수 있음
- 각 방에서 상하좌우 인접한 방으로 움직일 수 있음 

<입력>
- N (2<= N <= 100) : int, 방의 크기
- M (1<= M <= 20,000) : int, 스위치 개수 
- x,y,a,b : (x,y)방에서 (a,b)방의 스위치가 있음

<출력>
- int, 불을 켤 수 있는 방의 최대 개수

<풀이>
- 현재 있는 방에서 켤 수 있는 모든 방의 불을 킴 ..
- 새로 불을 켠 방의 인접한 4방향을 탐색하여 방문한 적이 있으면, 그 방에 갈 수 있으므로 큐 삽입
- 현재 있는 방의 인접한 방 중에 처음 방문하며 불이 켜져 있다면 이동, 큐 삽입, 방문처리


barn - 헛간의 방마다 불이 켜져 있는지 여부 (0: off, 1: on)
switches - 각 방마다 가지고 있는 스위치는 dict로 관리 
visited - 각 방의 방문 여부 
cnt - 불을 켤 수 있는 방의 개수 


'''