# https://www.acmicpc.net/problem/3151

import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
skills = list(map(int, input().split()))
answer = 0

skills.sort()

for i in range(N-2):
    l, r = i+1, N-1
    if skills[i] > 0:
        break
    
    while l < r:
        sum_value = skills[l] + skills[r] + skills[i]
        
        if sum_value > 0:
            r -= 1
        else:   
            if sum_value == 0:
                if skills[l] == skills[r]:
                    answer += (r-l)
                else:
                    answer += r-bisect_left(skills, skills[r])+1
            l += 1
print(answer)
