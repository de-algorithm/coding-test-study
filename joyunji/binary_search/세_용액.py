# https://www.acmicpc.net/submit/2473

import sys
input = sys.stdin.readline
N = int(input())
liquids = list(map(int, input().split()))

liquids.sort()


min_value = float('inf')
answer= [0, 0, 0]

for i in range(N-2):
    left, right = i+1, N-1
    while left < right:

        value = liquids[left] + liquids[right] + liquids[i]
    
        if abs(value) <= min_value:
            answer[0], answer[1], answer[2] = liquids[i], liquids[left], liquids[right]
            min_value = abs(value)

        if value <= 0:
            left += 1
        else:
            right -= 1
        

print(*sorted(answer))