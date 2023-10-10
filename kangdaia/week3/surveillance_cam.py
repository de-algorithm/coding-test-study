def surveillance_camera(routes: list[list[int]]) -> int:
    """
    고속도로를 이동하는 모든 차량이 고속도로를 이용하면서 단속용 카메라를 한 번은 만나도록 카메라를 설치하려고 합니다.
    고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때,
    모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return 한다.
    차량의 진입 지점, 진출 지점은 -30,000 이상 30,000 이하입니다.

    1. routes를 진출지점 기준으로 정렬함
    2. m 값은 max인 30000으로 시작, i는 단속카메라 수로 1로 시작함 (최소 개수)
    3. 각 루트로 for-loop:
    - 만약 진입시점이 m값보다 크면, 다른 말로 기존의 범위에서 벗어난 진입시점이면,
        - 카메라 대수를 증가시키고, m을 새로운 진출지점으로 업데이트
    - 매번 현재 진출지점과 m중 최소값으로 m을 업데이트

    Args:
        routes (list[list[int]]): 고속도로를 이동하는 차량의 경로 routes
                                    각각 [진입지점 int, 나간지점 int]

    Returns:
        int: 모든 차량이 한 번은 단속용 카메라를 만나도록 하는 최소 카메라 대수
    """
    routes.sort(key=lambda x: x[1])
    i = 1
    m = 30_000
    for s, e in routes:
        if s > m:
            i += 1
            m = e
        m = min(e, m)
    return i
