'''
https://www.acmicpc.net/problem/12015

입력
- 수열 A의 크기 N(int) : 1<= N <=1,000,000
- 수열 A를 이루고있는 숫자 : 1<= Ai <= 1,000,000

출력
- 수열 A의 가장 긴 증가하는 부분 수열의 길이 

LIS의 처음으로 등장하는 item보다 크거나 같은 수와 교체해줬을 때, 길이 자체는 변하게 하지 않으면서
뒤에 남은 탐색할 수들을 최대한 많이 담을 수 있다.
'''

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]

for num in A[1:]:
    # LIS의 가장 큰 수보다 클 때 
    if LIS[-1] < num:
        LIS.append(num)
        
    else:
        l, r = 0, len(LIS) -1 
        
        while l < r:
            m = (1+r)//2
            
            if LIS[m] < num:
                l = m+1
            else:
                r = m-1
        # 들어갈 자리에 있는 수가 num보다 크거나 같다면 num로 교체
        # 작다면 굳이 바꿀 필요가 없으니 다음 수를 i로 교체해준다.
            if LIS[m] >= num:
                LIS[m] = num
            else:
                LIS[m+1] = num
print(len(LIS))

