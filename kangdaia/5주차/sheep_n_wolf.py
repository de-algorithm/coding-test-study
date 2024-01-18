def survive(info: list[int], edges: list[list[int]]) -> int:
    """
    항상 늑대가 양의 갯수보다 적을 때, 모을 수 있는 양의 갯수의 최댓값을 구한다.
    1. 간선 DICT 형태로 정리
    2. travel_tree 함수로 재귀 구성
        - 주어진 노드의 info값을 확인해 양/늑대 구분
        - 늑대의 경우, 늑대 갯수 >= 양 갯수 면 멈춤
        - max 양의 수 갱신
        - 현재까지 방문한 노드를 추가하고, 현재까지 방문한 노드 기준 방문 가능한 모든 노드를 찾음
        - 방문가능한 노드들 중 이미 방문한 노드를 제외 후 재귀 호출

    Args:
        info (list[int]): 각 노드의 양과 늑대를 표시하는 리스트. 0은 양, 1은 늑대
        edges (list[list[int]]): 각 간선을 (시작, 끝) 형태로 담은 리스트

    Returns:
        int: 가장 많이 모을 수 있는 양의 수
    """
    global max_sheep
    node_list = dict()
    for edge in edges:
        node_list[edge[0]] = node_list.get(edge[0], list()) + [edge[1]]
    max_sheep = 0
    
    def travel_tree(node: int, sheep: int, wolf: int, possible: list[int]) -> None:
        global max_sheep
        if info[node] == 1:
            wolf += 1
        else:
            sheep += 1
        if wolf >= sheep:
            return
        max_sheep = max(max_sheep, sheep)
        next_possible = possible+[node]
        neighbors = []
        for x in next_possible:
            neighbors += node_list.get(x, [])
        for neighbor in neighbors:
            if neighbor not in next_possible:
                travel_tree(neighbor, sheep, wolf, next_possible)
    travel_tree(0, 0, 0, [])
    return max_sheep