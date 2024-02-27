n = int(input())

dp = [1 for _ in range(n+2)]
dp[1] = 3
dp[2] = 7

if n == 1: print(3)
else:
    for i in range(3, n+1):
        dp[i] = (2*dp[i-1] + dp[i-2]) % 9901
    print(dp[n])