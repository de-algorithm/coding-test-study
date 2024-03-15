import math


def solution(X: int, Y: int, sprinklers: set[list[int]]) -> float:
    """
    조건: 스프링클러는 반지름 1인 원에 물을 뿌릴 수 있음.

    Args:
        X (int): 땅의 가로 길이
        Y (int): 땅의 세로 길이
        sprinklers (list[str]): 스프링클러 위치 목록 'a b'

    Returns:
        float: 주어진 스프링클러가 작동하는 영역의 합
    """
    map_springs = [[0] * (X+1) for _ in range(Y+1)]
    for s_x, s_y in sprinklers:
        map_springs[s_y][s_x] = 1
    area = 0
    for i in range(Y):
        for j in range(X):
            center = map_springs[i][j] == 1
            diag = map_springs[i+1][j+1]
            vh = map_springs[i+1][j] + map_springs[i][j+1]
            if center + vh + diag == 1:
                area += math.pi / 4
            elif (vh == 1 and diag == 0) or (vh == 1 and center == 0):
                area += math.sqrt(3) / 4 + math.pi / 6
            elif center + vh + diag >= 2:
                area += 1
    return area

x, y = list(map(int,input().split()))
n = int(input())
sprinkler_map = set()
for i in range(n):
    sprinkler_map.add(tuple(map(int,input().split())))
result = solution(x, y, sprinkler_map)
print(round(result, 6))