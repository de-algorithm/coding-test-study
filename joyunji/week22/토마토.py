'''
problem: https://www.acmicpc.net/problem/7576
'''

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
box = []
zero_count = 0  # 처음 저장된 익지 않은 토마토의 개수 
for _ in range(M):
    line = list(map(int, input().split()))
    zero_count += line.count(0)
    box.append(line)

def solution(N, M, box, zero_count):
    answer = 0
    day = 0 
    
    # 토마토가 모두 익지 못할 경우 
    q = deque()
    visited = [[False for _ in range(N)] for _ in range(M)]
    # 익은 토마토를 찾아서 큐에 삽입
    for i in range(M):
        for j in range(N):
            if box[i][j] == 1 and visited[i][j] == False:
                q.append((i,j,day))
                visited[i][j] = True
    rippen_count = 0
    # 우, 하, 좌, 상 
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    # 큐에서 꺼낸 토마토의 주변 토마토를 익게 만듬
    while q:
        x, y, d = q.popleft()
        # 상우하좌 4 방향 탐색
        for k in range(4):
            # 상우하좌 위치 이동한 좌표값 
            nx, ny = x + dx[k], y + dy[k] 
            # 좌표값이 박스 내에 존재하고, 안익은 토마토이며, 방문한 적이 없다면 
            if 0 <= nx < M and 0 <= ny < N and box[nx][ny] == 0 and visited[nx][ny] == False:
                # 방문 처리 및 이동거리 누적 
                visited[nx][ny] = True
                box[nx][ny] = 1
                rippen_count += 1
                # 큐에 삽입
                q.append((nx,ny, d+1)) 
                answer = d+1
    
    # 모든 토마토가 익은 경우
    if zero_count == rippen_count:
        return answer
    # 익지 않은 토마토가 있는 경우
    elif zero_count > rippen_count:
        return -1
    
if zero_count == 0:
    print(0) # 저장될 때부터 토마토가 다 익은 경우
else:
    print(solution(N, M, box,zero_count))
    