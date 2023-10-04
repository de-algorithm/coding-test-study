def surveillance_camera(routes: list[list[int]]) -> int:
    """
    고속도로를 이동하는 모든 차량이 고속도로를 이용하면서 단속용 카메라를 한 번은 만나도록 카메라를 설치하려고 합니다.
    고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때,
    모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return 한다.
    차량의 진입 지점, 진출 지점은 -30,000 이상 30,000 이하입니다.

    Args:
        routes (list[list[int]]): 고속도로를 이동하는 차량의 경로 routes
                                    각각 [진입지점 int, 나간지점 int]

    Returns:
        int: 모든 차량이 한 번은 단속용 카메라를 만나도록 하는 최소 카메라 대수
    """
    routes.sort(key=lambda x: (x[1], x[0]))
    i = 1
    m = 30_000
    for s, e in routes:
        if s > m:
            i += 1
            m = e
        m = min(e, m)
    return i
