import sys
sys.stdin = open('yunji/input.txt', 'r')

input = sys.stdin
N = int(input.readline())
t = [0] * (N+1)
p = [0] * (N+1)
dp = [0] * (N+1)

for i in range(1, N+1):
    t[i], p[i] = map(int, input.readline().split())    

for i in range(1, N+1):
    dp[i] = max(dp[i-1], dp[i])
    if i+t[i]-1 <= N+1:
        dp[i+t[i]-1] = max(dp[i-1]+p[i], dp[i+t[i]-1])
print(dp[-1])
        