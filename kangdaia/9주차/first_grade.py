def correct_operator(numbers: list[int]) -> int:
    """1학년
    일반적인 재귀로는 기하급수적으로 많은 경우의 수를 계산할 수 없음 - 시간초과
    -> DP 사용.
    조건으로 0~20사이의 수만 사용한다고 제한했기 때문에,
    DP[i][j] = 경우의 수, i = number list index, j = 0~20 사이의 수
    1. init: dp[0][8] = 1
    2. 1 ~ len(number)-1 루프동안, numbers[i]에 대해
        - 0 ~ 20까지, 각 숫자 j에 대해,
            - 숫자 j와 numbers[i]를 합치고 뺀 숫자가 0에서 20 사이면
            - 이전 인덱스 (마지막 계산한 dp)에서 숫자 j와 numbers[i]를 합치고 뺀 숫자의 값 (경우의 수)을
                현재 인덱스 dp의 숫자 j에 추가
            -> ex) dp[0][8] = 1, dp[1][5] += dp[0][5+3], dp[1][11] += dp[0][11-3]
                   = 5, 11은 8과 3으로 만들 수 있는 두가지 수, 각각 경우의 수 = 1
    3. dp[-1][마지막 값]이 해당 값을 만드는 경우의 수를 담고 있음.

    Args:
        numbers (list[int]): 계산을 할 숫자 목록

    Returns:
        int: 마지막 숫자가 결과값일 때, 그 외 숫자로 만들 수 있는 경우의 수
    """
    final = numbers.pop()
    n = len(numbers)
    dp = [[0 for _ in range(21)] for _ in range(n)]
    dp[0][numbers[0]] = 1
    for i in range(1, n):
        for j in range(21):  # 0 ~ 20
            if j + numbers[i] <= 20:
                dp[i][j] += dp[i-1][j+numbers[i]]
            if j - numbers[i] >= 0:
                dp[i][j] += dp[i-1][j-numbers[i]]
    return dp[-1][final]


if __name__ == "__main__":
    input = ["11", "8 3 2 4 8 7 2 4 0 8 8"]
    transform = list(map(lambda x: int(x), input[1].split()))
    answer = correct_operator(transform)
    print(answer, answer == 10)

    input = ["3", "0 0 0"]
    transform = list(map(lambda x: int(x), input[1].split()))
    answer = correct_operator(transform)
    print(answer, answer == 2)

    input = ["40", "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 1"]
    transform = list(map(lambda x: int(x), input[1].split()))
    answer = correct_operator(transform)
    print(answer, answer == 7069052760)
