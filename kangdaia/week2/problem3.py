from collections import deque


def get_distance(x, y): # BFS
    queue = deque([(x, y)])
    visited = [[-1 for _ in range(len(area)+1)] for _ in range(len(area)+1)]
    visited[x][y] = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 < nx <= len(area) and 0 < ny <= len(area):
                if area[nx-1][ny-1] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[cx][cy] + 1
                    queue.append((nx, ny))
    return visited


def pickup_passenger(taxi, passengers):
    passenger_dist = get_distance(*taxi)
    passengers.sort(key=lambda p: (-passenger_dist[p[0]][p[1]], -p[0], -p[1]))
    passenger = passengers.pop()
    return passenger, passenger_dist[passenger[0]][passenger[1]]


def solution(fuel: int, board: list[list[int]], taxi: list[int], passengers: list[list[int]]) -> int:
    """ 백준 스타트 택시
    택시 위치와 여러 승객 정보가 주어졌을 때, 주어진 우선순위를 적용해 모든 승객을 태운 후
    남은 연료 량을 반환하는 프로그램
    승객 선택 우선 순위: 현위치에서 최단거리 < 행번호 작은 순 < 열번호 작은 순
    한칸당 1연료만큼 소모하며, 승객을 태워 도착지에 도착할 때, 연료량이 모자라지 않으면 소모한 연료양의 두배를 충전한다.
    승객 상관없이 이동 중 연료가 바닥나면 실패로 간주하고 -1을 반환한다.
    승객을 다 태우지 못해도 -1을 반환한다.
    Args:
        fuel (int): 주어진 연료량
        board (list[list[int]]): n*n 의 지도, 0은 빈칸, 1은 벽 (벽은 통행불가)
        taxi (list[int]): 택시 위치 열, 행
        passengers (list[list[int]]): 승객 정보, 순서대로 출발지 열, 행, 도착지 열, 행 정보이다.

    Returns:
        int: 남은 연료 량 if all passenger moved, else -1
    """
    global remain_fuel, area
    #  initialization
    remain_fuel = fuel # 남은 연료량
    area = board
    for _ in range(len(passengers)):
        passenger, dist = pickup_passenger(taxi, passengers)
        d_x, d_y, a_x, a_y = passenger
        remain_fuel -= dist
        if dist == -1 or remain_fuel < 0:
            remain_fuel = -1
            break
        # drop-off
        arrival_dist = get_distance(d_x, d_y)
        remain_fuel -= arrival_dist[a_x][a_y]
        if arrival_dist[a_x][a_y] == -1 or remain_fuel < 0:
            remain_fuel = -1
            break
        remain_fuel += arrival_dist[a_x][a_y] * 2
        taxi = [a_x, a_y]
    return remain_fuel

n, m, init_fuel = list(map(int,input().split()))
active_map = []
for _ in range(n):
    active_map.append(list(map(int,input().split())))
car_init = list(map(int,input().split()))
passenger_info = []
for _ in range(m):
    passenger_info.append(list(map(int,input().split())))
result = solution(init_fuel, active_map, car_init, passenger_info)
print(result)