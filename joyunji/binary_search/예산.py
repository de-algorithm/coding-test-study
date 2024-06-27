# https://www.acmicpc.net/problem/2512
import sys
input = sys.stdin.readline

N = int(input())
budgets = list(map(int, input().split()))
M = int(input())

answer = 0
budgets.sort()

if sum(budgets) <= M:
    print(budgets[-1])
else:
    # l은 1부터 가능함 
    l, r = 1, budgets[-1]

    while l <= r:
        m = (l+r)//2
        curr_sum = 0
        for budget in budgets:
            if budget < m:
                curr_sum += budget
            else:
                curr_sum += m
    
        if curr_sum <= M:
            answer = m
            l = m + 1
        else:
            r = m - 1
    
    print(answer)


'''
반례 
10
1 1 1 1 11 11 11 11 11 100
100
41
'''
