'''
Date        : 2024.01.09
Problem     : https://www.acmicpc.net/problem/1946
Tag         : 정렬
'''

import sys
sys.stdin = open("yunji/input.txt", "r")


# 1차 성적으로 정렬한 후, 2차로 비교하기
def func2(arr):
    cnt = 1 # 합격자의 수
    arr.sort()  # 1차 성적 기준으로 정렬
    max = arr[0][1]
    
    for i in range(1, len(arr)):
        if max > arr[i][1]:
            cnt += 1
            max = arr[i][1] # 중요!!
    return cnt

T = int(sys.stdin.readline())      # 테스트 케이스의 개수
for i in range(T):
    N = int(sys.stdin.readline())   # 지원자의 숫자
    arr = []
    for j in range(N):
        first_score, second_score = map(int, sys.stdin.readline().split())
        arr.append([first_score, second_score])


    print(func2(arr))
    

