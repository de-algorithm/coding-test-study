def shortest_dist(gems: list[str]) -> list[int]:
    """
    진열된 모든 종류의 보석을 적어도 1개이상 포함하는 가장 짧은 구간을 찾아서 구매한다.
    비교 조건: 탐색하면서 dict에 값을 추가한디. 그리고 dict key list lenght를 보석의 갯수와 비교한다.

    Args:
        gems (list[str]): 1번 진열대부터 진열대 번호 순서대로 나열된 보석 목록

    Returns:
        list[int]: 가장 짧은 구간의 시작 진열대 번호와 끝 진열대 번호를 목록으로 반환
    """
    gem_counts = {gems[0]: 1}
    gem_size = len(set(gems))
    i = j = 0
    smallest = [0, len(gems)]
    while i < len(gems) and j < len(gems):
        if len(gem_counts) < gem_size:
            j += 1
            if j == len(gems):
                break
            gem_counts[gems[j]] = gem_counts.get(gems[j], 0) + 1
        else:
            if j-i < smallest[1]-smallest[0]:
                smallest = [i+1, j+1]
            else:
                gem_counts[gems[i]] -= 1
                if gem_counts[gems[i]] == 0:
                    del gem_counts[gems[i]]    # count가 0이 되면 key가 없어야하므로 반드시 del
                i += 1

    return smallest
