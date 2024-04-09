'''
Date        : 2023.09.19
Update      : 2024.01.22
Problem     : https://school.programmers.co.kr/learn/courses/30/lessons/1844
Tag         : DFS/BFS
'''

from collections import deque
def solution(maps):
    """
    게임 맵에 대해서 BFS 수행하는 함수
    Args:
        maps (list): n x m 크기의 게임 맵의 상태가 들어있는 2차원 배열

    Returns:
        int: 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값
    """
    n = len(maps)       # 행
    m = len(maps[0])    # 열
    
    # 맵과 동일한 크기의 방문여부와 거리를 체크하기 위한 이중리스트
    visited = [[-1]*m for _ in range(n)] 
    
    # 큐 
    q = deque()
    
    q.append((0,0))     # 출발점 (0,0)부터 큐에 삽입 
    visited[0][0] = 1   # 출발점 (0,0)은 방문처리 
    
    # 하,우,상,좌   
    dx = [0,1,0,-1]     
    dy = [1,0,-1,0]
    
    # 큐가 빌 때까지 반복
    while q:
        x,y = q.popleft()   # 선입선출 
        
        # 상우하좌 4 방향 탐색
        for k in range(4):
            # 상우하좌 위치 이동한 좌표값 
            nx, ny = x + dx[k], y + dy[k] 
            # 좌표값이 맵 내에 존재하고, 벽이 아니며, 방문한 적이 없다면 
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == -1:
                # 방문 처리 및 이동거리 누적 
                visited[nx][ny] = visited[x][y]+1
                # 큐에 삽입
                q.append((nx,ny))
                
    return visited[n-1][m-1]