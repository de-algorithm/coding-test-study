# 필요한 만큼 나무를 자르기 위한 절단기의 최대 높이를 구하시오
# 나무 - 절단기 높이 만큼 잘림

import sys

#N = 나무 갯수, M= 필요한 나무 길이
N, M = map(int,sys.stdin.readline().split())

tree = list(map(int,sys.stdin.readline().split()))
start, end = 0, max(tree)

result = 0
while start <= end:
    mid = (start+end) // 2
    cut = 0

    for t in tree:
        if t - mid > 0:
            cut += t-mid

    if cut == M:
        print(mid)
        break
    # cutting 된 길이가 가져가야될 나무보다 더 크면
    # 절단기 길이를 더 늘려서 더 잘라야됨 
    if cut > M:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

else:  
    print(result)
