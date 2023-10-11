'''
Date        : 2023.10.10
Problem     : https://school.programmers.co.kr/learn/courses/30/lessons/64062
Tag         : 이분탐색
'''
def solution(stones, k):
    answer = 0
    
    left = 1                # 최소 1명이상 건널 수 있음
    right = max(stones) 
    
    while left <= right:
        mid = (left+right) // 2
        
        count = 0   # 건너뛰는 연속된 디딤돌의 개수
        
        # mid명이 디딤돌을 건널 때
        for i in range(len(stones)):
            # 0과 같거나 작아서 건널 수 없는 디딤돌이 있다면 건너뛰는 디딤돌 카운트
            if stones[i] <= mid:
                count +=1  
            else:               # 건널 수 있는 디딤돌이라면 count 초기화      
                if count > 0:
                    count = 0      
            
            # count가 K개와 같거나 크면 for문 탈출
            if count >= k:
                break
            
        # mid명이 건널 수 없는 경우   
        if count >= k:
            answer = mid 
            right = mid - 1
        # mid명이 건널 수 있는 경우
        else:
            left = mid + 1
            
    return answer

import sys
sys.stdin = open('yunji/input.txt', 'r')
stones = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())

print(solution(stones, k))