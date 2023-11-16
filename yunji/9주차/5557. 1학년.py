import sys
sys.stdin = open('yunji/input.txt', 'r')

input = sys.stdin
N = int(input.readline())
num = list(map(int, input.readline().split()))
dp = [[0 for _ in range(21)] for _ in range(N-1)]

dp[0][num[0]] = 1   # 첫번째 숫자에 대한 횟수?
for i in range(N-2):    # num[0] ~ num[n-3] 까지 
    for j in range(21): # dp[i]에서 계산값 0 ~20 까지의 횟수 저장을 위함
        if dp[i][j] > 0:
            if j+num[i+1] <= 20:
                dp[i+1][j+num[i+1]] += dp[i][j]
            if j-num[i+1] >= 0:
                dp[i+1][j-num[i+1]] += dp[i][j]

# for i in range(N-1):
#     print(num[i], dp[i])      
print(dp[-1][num[-1]])