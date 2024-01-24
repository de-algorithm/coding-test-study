'''
Date        : 2023.10.10
Problem     : https://www.acmicpc.net/problem/2805
Tag         : 이분탐색
'''

import sys
sys.stdin = open('yunji/input.txt', 'r')


N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
result = 0

left = 0     
right = max(trees)   # 가장 높은 나무의 길이

while left <= right:
    mid = (left + right) // 2
    
    sum = 0
    for tree in trees:
        if tree > mid:
            sum += tree - mid
            
    # print("Left:",left, " Right:",right)
    # print("나무 절단기:",mid)
    # print("sum:", sum)
    
    if sum >= M:
        left = mid + 1
        result = mid
    else:
        right = mid - 1


print(result)