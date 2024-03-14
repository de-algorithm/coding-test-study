def solution(n: int, x: list[int], a: list[int]) -> int:
    """수직선과 같은 일직선상에 N개의 마을이 위치해 있을 때, 
    각 사람들까지의 거리의 합이 최소가 되는 위치를 찾는다.
    case 1. 가중 평균 계산 round(sum([x[i]*a[i]for i in range(n)]) / sum(a))
    case 2. 누적 인구수가 절반을 넘어가는 지점 찾기

    Args:
        n (int): 마을 개수 (1 ≤ N ≤ 100,000)
        village (list[int]): 각 마을의 위치 (|X[i]| ≤ 1,000,000,000)
        people (list[int]): 각 마을의 사람 수 (1 ≤ A[i] ≤ 1,000,000,000)

    Returns:
        int: 각 사람들까지의 거리의 합이 최소가 되는 위치
    """
    village = list(map(lambda x_i, a_i: [x_i, a_i], x, a))
    village.sort(key=lambda elem: elem[0])  # x의 거리 기준 정렬
    total_people = sum(a)
    count = 0
    for i in range(n):
        count += village[i][1]
        if count >= total_people / 2:
            return village[i][0]