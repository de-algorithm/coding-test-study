# https://www.acmicpc.net/problem/2110
import sys
input = sys.stdin.readline

# N: 집의 개수, C: 공유기의 개수
N, C = map(int, input().split())
x = [int(input()) for _ in range(N)]


# 이분 탐색? 
# 가장 인접한 두 공유기 사이의 거리를 최대로 
x.sort()
left = 1
right = x[-1] - x[0]


while left <= right:
    mid = (left + right) // 2 # 두 인접한 공유기의 거리 
    install = x[0]
    count = 1
    
    # 현재 설치된 공유기와의 거리가 mid 이상인 경우에 공유기 설치 
    for i in range(1, len(x)):
        if x[i] >= install + mid:
            count += 1
            install = x[i]
            print(install)
    
    # 설치된 공유가 c이상이면 공유기 사이의 거리를 증가시킨다.
    if count >= C:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1
        
print(answer)