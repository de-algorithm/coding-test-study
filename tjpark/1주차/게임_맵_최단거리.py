# 상대 팀 진영 도착 최단거리 구하기 / 도착 못할 때 -1 반환
# bfs로 탐색하여 목표 도착 시 거리 반환
from collections import deque

def solution(maps):
    answer = 0
    
    # 지나간 길 check, 얼마나 지나갔는지 count
    row, col = len(maps), len(maps[0])
    visited = [[0]*col for _ in range(row)]
    
    # 방향 설정
    dir = [(0,1),(0,-1),(1,0),(-1,0)]
    
    # 초기 설정
    que = deque([[0,0]])
    visited[0][0] = 1 
    
    while que:
        my, mx = que.popleft()
        for dx, dy in dir:
            x = mx + dx
            y = my + dy
            
            # 맵 사이즈, 방문 여부, 장애물 check
            if 0<=x<col and 0<=y<row and visited[y][x] < 1 and maps[y][x]:
                visited[y][x] = visited[my][mx] + 1
                que.append([y,x])
                
                # 목표 지점 도착 시 거리 반환
                if x==col-1 and y==row-1:
                    return visited[y][x]
            
    return -1
