'''
Date        : 2023.10.11
Problem     : https://www.acmicpc.net/problem/11052
Tag         : DP
'''
import sys
sys.stdin = open('yunji/input.txt', 'r')

N = int(sys.stdin.readline())                              # 카드 N개
P = [0] + list(map(int, sys.stdin.readline().split()))    # 카드팩 가격 

dp = P[:]       # 원래의 카드팩 가격 복사

for i in range(2, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j]+dp[j])

print(dp[-1])


