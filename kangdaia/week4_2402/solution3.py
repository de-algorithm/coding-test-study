import math
from collections import defaultdict, deque


def solution(X: int, Y: int, sprinklers: list[str]) -> float:
    """
    조건: 스프링클러는 반지름 1인 원에 물을 뿌릴 수 있음.

    Args:
        X (int): 땅의 가로 길이
        Y (int): 땅의 세로 길이
        sprinklers (list[str]): 스프링클러 위치 목록 'a b'

    Returns:
        float: 주어진 스프링클러가 작동하는 영역의 합
    """
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    diagonal_x, diagonal_y = [-1, 1, 1, -1], [1, 1, -1, -1]
    sp_coords = []
    overlap = set()
    total_area = overlap_area = 0
    # string 형태의 좌표를 리스트로 변환
    for sprinkler in sprinklers:
        a, b = map(int, sprinkler.split())
        sp_coords.append((a, b))
    # 각 좌표마다 겹치지 않는 범위의 각도와 겹치는 영역이 있는지 확인
    for a, b in sp_coords:
        angle = 360
        if not(0 < a < X and 0 < b < Y): # 테두리
            if a in [0, X] and b in [0, Y]:
                angle = 90
            else:
                angle = 180
        # 겹치는 영역이 있을 경우, 가로세로는 120도, 대각선은 90도로 겹침
        # 겹치는 영역이 있는 좌표를 overlap에 추가
        next_move = map(lambda _dx, _dy: (a+_dx, b+_dy), dx, dy)
        next_diagonal = map(lambda _dx, _dy: (a+_dx, b+_dy), diagonal_x, diagonal_y)
        for n_a, n_b in next_move:
            if (n_a, n_b) in sp_coords:
                angle -= 120
                overlap.add((n_a, n_b, 120))
        for n_a, n_b in next_diagonal:
            if (n_a, n_b) in sp_coords:
                angle -= 90
                overlap.add((n_a, n_b, 90))
        total_area += math.pi * (angle/360) # 겹치지 않는 영역만 합산
    # overlap에 있는 겹치는 영역만 계산 후 나누기 2
    for _, _, angle in overlap:
        if angle == 90:
            overlap_area += 1
        else:
            overlap_area += math.sqrt(3)/2

    return total_area + overlap_area/2


print(solution(4, 5, ["0 0", "4 4",]))
print(solution(10, 3, ["5 1", "6 1",]))
print(solution(7, 7, ["3 2", "2 2", "1 1", "6 3"]))