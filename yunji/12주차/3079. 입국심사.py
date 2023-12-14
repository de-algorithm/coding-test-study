'''
이분탐색?


'''

import sys
sys.stdin = open('yunji/input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())    # N개, M명
times = [int(input()) for _ in range(N)]

left = 1
right = max(times) * M  # 최대로 걸리는 시간

while left <= right:
    mid = (left + right) // 2
    
    # 임의의 시간동안 심사 가능한 사람 수 (total)
    # = 임의의 시간 // 각 심사대에서  심사하는데 걸리는 시간
    total = 0 
    for time in times:
        total += (mid // time)
        
        # 모든 심사대를 거치지 않아도 mid분 동안 M명 이상의 심사를 할 수 있는 경우는 반복문 탈출 
        if total >= M:
            break

    if total >= M:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
        

print(answer)