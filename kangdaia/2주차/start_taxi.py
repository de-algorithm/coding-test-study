"""
첫 줄에 N, M, 그리고 초기 연료의 양이 주어진다.
(2 ≤ N ≤ 20, 1 ≤ M ≤ N2, 1 ≤ 초기 연료 ≤ 500,000)

fuel: int
map: [[int]] ; n*n board, 0은 빈칸, 1은 벽
s_coord: [int, int] ; taxi starting coordinate, 행, 열
passenger_records: [[int, int, int, int]] ; m명의 승객 정보
승객 선택 우선 순위: 현위치 최단거리 위치 < 행번호 작은 순 < 열번호 작은 순 (행과 열 번호는 1 이상 N 이하의 자연)
태워 이동시 소모한 연료양의 두배를 충전 - 한칸당 1만큼 소모
이동 도중 연료 바닥나면 실피 -> 업무 끝
return 남은 연료 량 if all passenger moved, else -1

case 1. 다익스트라 알고리즘 적용하기
"""
import heapq


def start_taxi_route(fuel: int, board: list[str], taxi: str, passengers: list[str]) -> int:
    #  init
    start_row, start_col = list(map(lambda x: int(x)-1, taxi.split()))
    remain_fuel = fuel
    min_dist = []
    heapq.heappush(min_dist, (0, start_col, start_row))
    arrival_point = None
    work_done = 0
    visited = []
    passenger_dict = dict()
    for passenger in passengers:
        travel_info = list(map(lambda x: int(x)-1, passenger.split()))
        passenger_dict[(travel_info[0], travel_info[1])] = (travel_info[2], travel_info[3])
    
    while remain_fuel > -1 and work_done < len(passengers):
        if min_dist is None:
            return -1
        curr = heapq.heappop(min_dist)
        (curr_dist, curr_col, curr_row) = curr
        if arrival_point is not None and (curr_row, curr_col) == arrival_point:
            if remain_fuel - curr_dist < 0:
                remain_fuel = -1
                break
            remain_fuel += curr_dist
            work_done += 1
            arrival_point = None
            curr_dist = 0
        elif arrival_point is None and (curr_row, curr_col) in passenger_dict and (curr_row, curr_col) not in visited:
            if remain_fuel - curr_dist < 0:
                remain_fuel = -1
                break
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
