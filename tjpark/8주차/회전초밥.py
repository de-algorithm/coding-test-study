# 연속한 k개의 접시를 먹을경우 할인
# 특정 초밥 할인 쿠폰, 초밥 1개 무료 제공
# 해당 초밥이 벨트 위에 없으면 새로 만들어 제공

# input
# N= 초밥 벨트 상태, d= 초밥의 가짓수
# k=연속으로 먹을 수 있는 접시수, c= 쿠폰번호


import sys
from collections import defaultdict

sys_input = sys.stdin.readline
N, d, k, c = map(int,sys_input().split())

# 초밥 count용 dict
dic = defaultdict(int)
# 초밥 순서 저장용 list
table = []
# 초밥종류
dist_val = 1
# 초밥종류 최댓값 저장
max_val = -1

for i in range(N+k-1):
    # 회전하기 전
    if i < N:
        n = int(sys_input())
    # 한 바퀴 회전했을 때
    else:
        n = table[i-N]
    table.append(n)
    dic[n] += 1
    # 쿠폰x, 없었던 초밥이 count되면 종류개수 +1
    if dic[n] == 1 and n != c:
            dist_val += 1

    if i >= k:
        prev_n = table[i-k]
        dic[prev_n] -= 1
        if dic[prev_n] == 0 and prev_n != c:
            dist_val -= 1

    max_val = max(max_val,dist_val)
    if max_val == k+1:
        break

print(max_val)