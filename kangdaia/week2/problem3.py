import heapq


def solution(fuel: int, board: list[str], taxi: str, passengers: list[str]) -> int:
    """ 백준 스타트 택시
    택시 위치와 여러 승객 정보가 주어졌을 때, 주어진 우선순위를 적용해 모든 승객을 태운 후
    남은 연료 량을 반환하는 프로그램

    승객 선택 우선 순위: 현위치에서 최단거리 < 행번호 작은 순 < 열번호 작은 순
    한칸당 1연료만큼 소모하며, 승객을 태워 도착지에 도착할 때,
    연료량이 모자라지 않으면 소모한 연료양의 두배를 충전한다.
    승객 상관없이 이동 중 연료가 바닥나면 실패로 간주하고 -1을 반환한다.
    승객을 다 태우지 못해도 -1을 반환한다.

    다익스트라 알고리즘

    Args:
        fuel (int): 주어진 연료량
        board (list[str]): n*n 의 지도, 0은 빈칸, 1은 벽 (벽은 통행불가)
        taxi (str): 택시 위치 열, 행
        passengers (list[str]): 승객 정보, 순서대로 출발지 열, 행, 도착지 열, 행 정보이다.

    Returns:
        int: 남은 연료 량 if all passenger moved, else -1
    """
    #  initialization
    start_row, start_col = list(map(lambda x: int(x)-1, taxi.split()))
    remain_fuel = fuel # 남은 연료량
    min_dist = [] # 최단거리 큐 initialization
    heapq.heappush(min_dist, (0, start_col, start_row))
    arrival_point = None # 현재 이동 중인 승객의 도착지
    work_done = 0 # 이동 완료한 승객 수
    visited = [] # 이동한 승객 정보
    # 승객정보 딕셔너리로 변경, key가 출발지, value가 도착지
    passenger_dict = dict() 
    for passenger in passengers:
        travel_info = list(map(lambda x: int(x)-1, passenger.split()))
        passenger_dict[(travel_info[0], travel_info[1])] = (travel_info[2], travel_info[3])

    while remain_fuel > -1 and work_done < len(passengers):
        if min_dist is None: # 큐가 더이상 이동할 곳 이 없을 때,
            return -1
        curr = heapq.heappop(min_dist)
        (curr_dist, curr_col, curr_row) = curr
        # 도착지 위치를 찾은 경우
        if arrival_point is not None and (curr_row, curr_col) == arrival_point:
            if remain_fuel - curr_dist < 0: # 더이상 이동 불가
                return -1
            remain_fuel += curr_dist
            work_done += 1
            arrival_point = None
            curr_dist = 0
        # 출발지 위치를 찾은 경우
        elif arrival_point is None and (curr_row, curr_col) in passenger_dict and (curr_row, curr_col) not in visited:
            if remain_fuel - curr_dist < 0: # 더이상 이동 불가
                return -1
            remain_fuel -= curr_dist
            arrival_point = passenger_dict[(curr_row, curr_col)]
            visited.append((curr_row, curr_col))
            curr_dist = 0

        if remain_fuel - curr_dist > 0:
            left = board[curr_row].split()[curr_col-1] if curr_col-1 >= 0 else "1"
            heapq.heappush(min_dist, (1+curr_dist, curr_col-1, curr_row)) if left != "1" else 0
            right = board[curr_row].split()[curr_col+1] if curr_col+1 < len(board) else "1"
            heapq.heappush(min_dist, (1+curr_dist, curr_col+1, curr_row)) if right != "1" else 0
            top = board[curr_row-1].split()[curr_col] if curr_row-1 >= 0 else "1"
            heapq.heappush(min_dist, (1+curr_dist, curr_col, curr_row-1)) if top != "1" else 0
            bottom = board[curr_row+1].split()[curr_col] if curr_row+1 < len(board) else "1"
            heapq.heappush(min_dist, (1+curr_dist, curr_col, curr_row+1)) if bottom != "1" else 0

    return remain_fuel
