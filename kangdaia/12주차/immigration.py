def austrailia(m: int, n: int, times: list[int]) -> int:
    """_summary_

    Args:
        m (int): 심사할 사람 수
        n (int): 입국심사대 수
        times (list[int]): 각 입국심사관들의 한사람 당 심사시간

    Returns:
        int: 모든 사람이 심사를 받는데 걸리는 최소 시간
    """
    dp = list(range(0, n)) # 입국심사대

    return 0


if __name__ == "__main__":
    # general test
    # test 1
    result = austrailia(2, 6, [7, 10])
    print(result, result == 28)
    # test 2
    result = austrailia(7, 10, [3, 8, 3, 6, 9, 2, 4])
    print(result, result == 8)
