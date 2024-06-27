'''
- 빌딩 가장자리 벽이 아닌 곳으로 빌딩 안팍을 드나들 수 있음
- 각각의 문에 대해 열쇠는 0개 이상, 각각의 열쇠에 대해서 문은 0개 이상임
- 상근이가 훔칠 수 있는 문서의 최대 개수 

# 빌딩 가장자리 빈 공간으로 들어감
# $를 찾음, 소문자를 보면 열쇠 저장 후 이동, 대문자를 보면 해당 문의 열쇠가 있다면 이동 
'''
from collections import defaultdict, deque
import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    door = defaultdict(int)
    h, w = map(int, input().split())
    building = []
    # 테두리에 빈 공간 추가
    building.append(['.']*(w+2))
    for _ in range(h):
        building.append(list('.'+input().strip()+ '.'))
    building.append(['.']*(w+2))

    # 열쇠 저장 
    keys = input().strip()
    if keys != '0':
        for key in keys:
            door[key.upper()] += 1


    cnt = 0
    dx = (0,0,1,-1)
    dy = (1,-1,0,0)

    def bfs(x,y):
        q = deque()
        visited = [[0]*(w+2) for _ in range(h+2)] 
        global cnt
        
        q.append((x,y))
        visited[x][y] = 1
        
        while q:
            x, y = q.popleft()
            
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0 <= nx < h+2 and 0 <= ny < w+2 and building[nx][ny] != '*' and visited[nx][ny] == 0:
                    if building[nx][ny] == '$':
                        cnt += 1
                        building[nx][ny] = '.'
                        q.append((nx, ny))
                        visited[nx][ny] = 1
                    elif building[nx][ny] == '.':
                        q.append((nx, ny))
                        visited[nx][ny] = 1
                    elif building[nx][ny].islower(): # 열쇠일 때
                        if door[building[nx][ny].upper()] == 0:
                            door[building[nx][ny].upper()] += 1
                            visited = [[0]*(w+2) for _ in range(h+2)]  # 방문기록 초기화 
                        building[nx][ny] = '.'
                        visited[nx][ny] = 1
                        q.append((nx, ny))
                    elif building[nx][ny].isupper(): # 문 일때
                        if door[building[nx][ny]] > 0:
                            building[nx][ny] = '.'
                            q.append((nx, ny))
                            visited[nx][ny] = 1
                    
    bfs(0,0)
    print(cnt)