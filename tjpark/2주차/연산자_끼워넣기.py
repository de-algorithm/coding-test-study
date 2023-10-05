# 숫자와 연산자를 조합해 최댓값과 최솟값 구하기
# 정해진 숫자 순서, 정해진 연산자 사용 갯수(순서상관 x)를 입력으로 받음
# 1. 모든 연산 값을 구해보기 (완전탐색)
# 2. 최댓값, 최솟값을 구하기 위한 공식 생각해서 prunning 해보기 (적용 힘듦)

import sys

N = int(sys.stdin.readline())
num, cal_list = [list(map(int,sys.stdin.readline().split())) for _ in range(2)] 
# 초기값 설정
result_min, result_max = 1000000000, -100000000

# dfs 구동 방식
# 연산자 갯수 만큼 계산진행
# 재귀함수로 모든 연산 조합 결과를 구하고 최대, 최소 비교  
def dfs(prev_result, next_idx):
    # 최종 결과 값 비교를 위해 전역변수 설정
    global result_min, result_max

    if next_idx < N:
        '''
        기존 코드
        if cal_list[0]:  # 더하기
            cal_list[0] -= 1
            cal_result = prev_result + num[next_idx]
            dfs(cal_result, next_idx + 1)
            cal_list[0] += 1
        if cal_list[1]:  # 빼기
            cal_list[1] -= 1
            cal_result = prev_result - num[next_idx]
            dfs(cal_result, next_idx + 1)
            cal_list[1] += 1
        if cal_list[2]:  # 곱하기
            cal_list[2] -= 1
            cal_result = prev_result * num[next_idx]
            dfs(cal_result, next_idx + 1)
            cal_list[2] += 1
        if cal_list[3]:  # 나누기
            cal_list[3] -= 1
            cal_result = int(prev_result / num[next_idx])
            dfs(cal_result, next_idx + 1)
            cal_list[3] += 1
        '''
        # 반복 코드 줄이기
        for i, cal in enumerate(cal_list):
            if cal > 0:
                cal_list[i] -= 1
                if i == 0:  # 더하기
                    cal_result = prev_result + num[next_idx]
                elif i == 1:  # 빼기
                    cal_result = prev_result - num[next_idx]
                elif i == 2:  # 곱하기
                    cal_result = prev_result * num[next_idx]
                elif i == 3:  # 나누기
                    cal_result = int(prev_result / num[next_idx])
                
                dfs(cal_result, next_idx + 1)
                cal_list[i] += 1
    
    # 마지막 숫자 연산 시 최소, 최대 비교
    else:
        result_min = min(result_min, prev_result)
        result_max = max(result_max, prev_result)

result = dfs(num[0], 1)

print(result_max)
print(result_min)



