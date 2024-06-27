'''
https://www.acmicpc.net/problem/7453

입력
- 배열의 크기 n (int) : 1<= n <= 4000
- |배열에 들어있는 정수| <= 2^28 

출력
- 합이 0이 되는 쌍의 개수 

제한 12초

a+b+c+d = 0
1. (a+b) = -(c+d)
a+b 값, c+d 값 찾아두고
이분탐색으로 (a+b) + (c+d) = 0인 값 찾기 


'''
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ab, cd = [], []
for i in range(n):
    for j in range(n):
        ab.append(arr[i][0] + arr[j][1])
        cd.append(arr[i][2] + arr[j][3])


ab.sort()
cd.sort()

answer = 0
l, r = 0, len(cd) -1
print(ab)
print(cd)
while l < len(ab) and r >= 0:
    if ab[l] + cd[r] == 0:
        # ab, cd 중복 개수에 따른 answer 갱신
        next_l = bisect_right(ab, ab[l]) 
        next_r = bisect_left(cd, cd[r])
        answer += (next_l-l)*(r-next_r+1)
        
        l, r = next_l, next_r
        
    elif ab[l] + cd[r] > 0:
        r -= 1
    else:
        l += 1   
        
print(answer)