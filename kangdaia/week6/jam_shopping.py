def shortest_dist(gems: list[str]) -> list[int]:
    """
    진열된 모든 종류의 보석을 적어도 1개이상 포함하는 가장 짧은 구간을 찾아서 구매한다.

    Args:
        gems (list[str]): 1번 진열대부터 진열대 번호 순서대로 나열된 보석 목록

    Returns:
        list[int]: 가장 짧은 구간의 시작 진열대 번호와 끝 진열대 번호를 목록으로 반환
    """
    gem_kinds = set(gems)

    idx_range = []
    gem_count = set()

    i = j = 0

    while j < len(gems):
        search = gems[i:j+1]
        if len(search) < len(gem_kinds):
            j += 1
    return [i, j]