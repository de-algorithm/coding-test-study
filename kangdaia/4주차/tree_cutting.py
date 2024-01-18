def wood_cutter(req_lenth: int, trees: str) -> int:
    """_summary_

    Args:
        req_lenth (int): 가져가려고 하는 나무의 길이 m
        trees (str): 스페이스로 구분된 각 나무의 높이를 담은 스트링

    Returns:
        int: 적어도 필요한 길이의 나무를 갖기위한 절단기 최대 높이
    """
    tree_list = list(map(lambda x: int(x), trees.split()))
    answer = 0
    low, high = min(tree_list), max(tree_list)
    while low <= high:
        mid = (low+high)//2
        rest_tree = sum(list(map(lambda x: x-mid if x-mid >= 0 else 0, tree_list)))
        if rest_tree < req_lenth:
            high = mid - 1
        else:
            answer = max(answer, mid)
            low = mid + 1
    return answer
