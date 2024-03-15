def solution(N: int, costs: list[list[int]]) -> int:
    dp = [[0] * 3 for _ in range(N)]
    dp[0] = costs[0]
    for i in range(1, N):
        r, g, b = costs[i]
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + r
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + g
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + b
    return min(dp[N-1])

n = int(input())
color_cost = []
for i in range(n):
    color_cost.append(list(map(int,input().split())))
result = solution(n, color_cost)
print(result)