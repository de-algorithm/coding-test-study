def solution(n: int, works: list[list[int]]) -> int:
    """ 퇴사2

    Args:
        n (int): 일을 해결할 최대 기간
        works (list[str]): 각 인덱스가 i+1 날일 때, 소요 일수와 일의 수당을 string으로 담은 목록

    Returns:
        int: 최대로 얻을 수 있는 수당(이득)
    """
    profit = 0
    dp = [0] * (n+1)
    for day in range(n):
        profit = max(profit, dp[day])
        if day + works[day][0] <= n:
            dp[day+works[day][0]] = max(profit+works[day][1], dp[day+works[day][0]])
    return max(dp)


N = int(input())
w = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, w))