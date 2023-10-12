# 카드 N개가 포함된 카드팩
# 돈을 최대한 많이 지불해서 카드 N개 구매하려고 한다.
# 카드 개수 합이 N개인 P의 최댓값을 구하기

import sys

N = int(sys.stdin.readline())

# dp풀이 

# 계산을 편하게 하기 위해 0번 인덱스 추가
P = [0] + list(map(int,sys.stdin.readline().split()))
dp = [0] * (N+1)

for i in range(1,N+1):
    for j in range(1, i+1):
        # dp[i] = i개의 카드를 얻기 위해 지불해야 하는 최대 금액
        dp[i] = max(dp[i-j]+P[j],dp[i])
#print(dp)
print(dp[N])


'''
# 31% error code
# 반례
# 10
# 1 1 1 1 10 13 1 1 1 1

# P의 카드 하나당 얼만지 계산 후 정렬
# 카드 하나당 값이 큰 것 부터 계산해나감


p_list = [[p/(i+1),i+1] for i,p in enumerate(P)]
p_list.sort(key= lambda x: x[0], reverse=True)
print(p_list)
result = 0
for p in p_list:

    price, card_num = p

    if N / card_num >= 1:
        n = (N // card_num)
        result += price * card_num * n
        N -= card_num * n
    if N == 0:
        print(int(result))
        break
'''



