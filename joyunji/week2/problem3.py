from collections import deque
import sys
# sys.stdin = open("yunji/input.txt", "r")
input = sys.stdin 
N, M, fuel = map(int, input.readline().split())
maps = [ list(map(int,(input.readline().split()))) for _ in range(N)]
driver_X, driver_Y = map(int, input.readline().split())
passengers = [list(map(int,(input.readline().split()))) for _ in range(M)]

# print(N, M, fuel)
# print(maps)
# print(driver_X, driver_Y)
# print(passengers)

def bfs(N, maps, start_X, start_Y, dest_X, dest_Y):
    
    q = deque()
    visited = [[-1]*(N) for _ in range(N)]
    
    q.append((start_X-1, start_Y-1))
    visited[start_X-1][start_Y-1] = 0
    
    # 하,우,상,좌
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    while q:
        x, y = q.popleft()
        if x == dest_X-1 and y == dest_Y-1:
            return visited[x][y]
        
        # 상우하좌 4 방향 탐색
        for k in range(4):
            # 상우하좌 위치 이동한 좌표값 
            nx, ny = x + dx[k], y + dy[k] 
            
            # 좌표값이 맵 내에 존재하고, 벽이 아니며, 방문한 적이 없다면 
            if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] == 0 and visited[nx][ny] == -1:
                # 방문 처리 및 이동거리 누적 
                visited[nx][ny] = visited[x][y]+1
                # 큐에 삽입
                q.append((nx,ny)) 
                
    return visited[dest_X-1][dest_Y-1]
    

def solution(N, M, fuel, maps, driver_X, driver_Y, passengers):
    # N개 줄 지도
    # M명의 승객 
    # 기사가 있는 곳에 가장 가까운 위치에 있는 승객까지의 최단 거리 a
    # 해당 승객의 위치에서 목적지까지 최단 거리 b
    # 현재 연료 >= a+b 라면 해당 승객은 데려다줄 수 있는 것으로 간주
    #   기사 위치 <= 목적지, 현재 연료 <= 현재 연료-(a+b)+2b 갱신
    # 아니라면 -1을 반환
    
    p_dict = {i:passengers[i] for i in range(M)}

    # 승객 수만큼 반복 
    while p_dict:
        # 기사 -> 승객
        # 현재 남아있는 승객 중 가장 최단거리에 있는 승객 탐색
        shortest_dist_to_a = int(1e9) # 현재 기사와 승객의 최단거리
        idx = -1    # 최단거리에 있는 승객 번호
        for i in p_dict:    
            dist = bfs(N, maps, driver_X, driver_Y, p_dict[i][0], p_dict[i][1])
            # print(i+1,"번 승객까지의 거리: ", dist)
            if dist == -1:  # 승객을 태우러 갈 방법이 없을 경우 
                return -1
            
            if shortest_dist_to_a > dist:
                shortest_dist_to_a = dist
                idx = i
        

        # print(idx+1,"번 승객에게로 가는 중...")
        # 기사, 승객 -> 목적지 
        shortest_dist_to_b = bfs(N, maps, p_dict[idx][0], p_dict[idx][1], p_dict[idx][2], p_dict[idx][3])
        
        # 현재 연료에서 승객을 태우러 가고 목적지에 데려다 준 후 남은 연료가 없을 때
        if fuel < shortest_dist_to_a+shortest_dist_to_b:
            return -1
        
        fuel = fuel-(shortest_dist_to_a+shortest_dist_to_b)+2*shortest_dist_to_b    
        driver_X, driver_Y = p_dict[idx][2], p_dict[idx][3] # 기사의 출발 위치를 승객을 데려다준 목적지로 변경
        p_dict.pop(idx)   # 이동 완료한 승객은 승객 리스트에서 삭제

    return fuel


print(solution(N, M, fuel, maps, driver_X, driver_Y, passengers))