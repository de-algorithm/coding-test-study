def locate_lion(size: int) -> int:
    dp = [[0, 0, 0] for _ in range(size)]
    dp[0] = 3
    dp[1] = 3+2+2
    # 한마리도 배치하지 않는 방법 1가지, 1마리를 각각 왼쪽과 오른쪽에 넣는 2가지 방법, 각 줄에 2마리는 거주 불가 최대 1마리까지
    # 선택지-> 0마리, 왼쪽1마리, 오른쪽1마리
    # 앞에 0마리 -> 0마리, 왼쪽 1마리, 오른쪽 1마리
    # 앞에 왼쪽 1마리 -> 0마리, 오른쪽 1마리
    # 앞에 오른쪽 1마리 -> 0마리, 왼쪽 1마리
    for row_num in range(2, size):
        dp[row_num] = dp[row_num-1] * 2 + dp[row_num-2]

    return dp[size-1] % 9901


if __name__ == "__main__":
    result = locate_lion(4)
    print(result, result == 41)