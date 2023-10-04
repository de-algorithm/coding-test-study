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
"""


def find_dist(curr, end, board):
    dist_cand = []

    def dist_calc(curr, end, dist=0):  # [6, 5]
        if curr[0] == len(board) or curr[1] == len(board) or curr[0] < 0 or curr[1] < 0:
            return 0
        if curr[0] == end[0] and curr[1] == end[1]:
            dist_cand.append(dist)
            return 0
        curr_row, curr_col = curr
        if board[curr_row - 2][curr_col - 1] == 0:  # top
            dist_calc([curr_row - 2, curr_col - 1], end, dist + 1)
        if board[curr_row][curr_col - 1] == 0:  # bottom
            dist_calc([curr_row, curr_col - 1], end, dist + 1)
        if board[curr_row - 1][curr_col - 2] == 0:  # left
            dist_calc([curr_row - 1, curr_col - 2], end, dist + 1)
        if board[curr_row - 1][curr_col] == 0:  # right
            dist_calc([curr_row - 1, curr_col], end, dist + 1)

    dist_calc(curr, end)
    return find_dist


def start_taxi_route(fuel, board, s_coord, passenger_records):
    curr_fuel = fuel
    taxi = s_coord

    record_w_dist = list(
        map(
            lambda rec: [
                rec[0],
                rec[1],
                rec[2],
                rec[3],
                find_dist(taxi, [rec[0], rec[1]], board),
            ],
            passenger_records,
        )
    )
    while curr_fuel >= 0:
        next_pass_cand = sorted(record_w_dist, key=lambda x: (x[4], x[0], x[1]))
        next_pass = next_pass_cand.pop(0)
        if next_pass[4] <= curr_fuel:
            curr_fuel += next_pass[4]
            taxi = [next_pass[2], next_pass[3]]
        else:
            curr_fuel = -1
        record_w_dist = list(
            map(
                lambda rec: [
                    rec[0],
                    rec[1],
                    rec[2],
                    rec[3],
                    find_dist(taxi, [rec[0], rec[1]], board),
                ],
                next_pass_cand,
            )
        )

    return curr_fuel
