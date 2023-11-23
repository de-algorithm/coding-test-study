def locate_lion(size: int) -> int:
    """
    find method to locate lion on the 2*n size board.
    lion cannot be on next to each ceil. (left != right)

    선택지: 0마리, 왼쪽 1마리, 오른쪽 1마리

    첫번째 줄 선택지: 3가지 (전체)
    두번째 줄 선택지:
    - 앞에 0마리: 전체 선택 (3)
    - 앞에 왼쪽 1마리: 0마리, 오른쪽 1마리 (2)
    - 앞에 오른쪽 1마리: 0마리, 왼쪽 1마리 (2)
    => 7가지
    세번째 줄 선택지:
    - 7가지 경우에 대한 선택지
    - 3+2+2+3+2+3+2 = (3+2+2)*2 + 3
    => 17가지

    Args:
        size (int): 2*size board

    Returns:
        int: method to locate lions remains by division of 9901
    """
    dp = [[0, 0, 0] for _ in range(size)]
    dp[0] = 3
    dp[1] = 3+2+2
    for row_num in range(2, size):
        dp[row_num] = dp[row_num-1] * 2 + dp[row_num-2]

    return dp[size-1] % 9901


if __name__ == "__main__":
    result = locate_lion(4)
    print(result, result == 41)