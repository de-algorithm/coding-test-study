n = int(input())
t, p = [0] * n, [0] * n
for i in range(n):
    t[i], p[i] = map(int, input().split())

dp = [0] * n

for i in range(n):
    dp[i] = max(dp[i], dp[i-1])

    fin_date = t[i] + i - 1
    if fin_date < n:
        dp[fin_date] = max(dp[fin_date], dp[i-1] + p[i])

print(max(dp))