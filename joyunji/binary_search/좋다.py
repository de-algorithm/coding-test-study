import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))

good_nums = defaultdict(bool)
answer = 0

for i in range(N):
    
    # A[i]가 좋은 수라고 판별나있다면 skip
    if good_nums[A[i]]:
        answer += 1
        continue

    l, r = 0, N-1

    # i가 마지막 인덱스인 경우 r을 N-2로 지정 
    if i == N-1:
        r = N-2
    if i == 0:
        l = 1
        
    while l < r:
        
        if l == i:
            l += 1
        if r == i:
            r -= 1
            
        if l >= r:
            break
            
        sum_value = A[l] + A[r]

        if A[i] < sum_value:
            r -= 1
        elif A[i] > sum_value:
            l += 1
        else:
            if not good_nums[A[i]]:
                good_nums[A[i]] = True
                answer += 1
                print(A[i], A[l],A[r])
                break

print(answer)


'''
반례

0 0 0 0 -> 4
-2 -1 -1 0 1 -> 4
0 0 1 -> 0
'''