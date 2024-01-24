'''
보석 : M가지 서로 다른 색상 (ex : Red 4개, Blue 7개)
모든 보석을 N명의 학생들에게 나누어 주려고 한다. 
이때, 보석을 받지 못하는 학생이 있어도 된다. 
하지만 학생은 항상 같은 색상의 보석만 가져간다. (학생 5명일 때, RR, RR, BB, BB, BBB(최대) => 질투심 3)

질투심이 최소가 되도록 보석을 나누어주는 방법
'''

import sys
from math import ceil

sys.stdin = open('yunji/input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split()) # N : 학생 수, M : 보석 종류 수
jewels = [int(input()) for _ in range(M)]

left = 1
right = max(jewels)


while left <= right:
    mid = (left + right) // 2   # mid : 한 사람이 가져가는 보석 수 
    sum = 0
    print("mid", mid)
    for jewel in jewels:
        print(ceil(jewel/mid))
        sum += ceil(jewel/mid) # sum : 보석을 나눠준 사람 수 합 

    if sum > N:
        left = mid + 1
    else:
        right = mid - 1

print(left)
