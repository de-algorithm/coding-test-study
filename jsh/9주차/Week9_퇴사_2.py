
# 날짜는 1일부터 시작하기떄문에 0번인덱스에 0으로 미리 하나 선언 후 요일수와 인덱스와 맞춰 진행

# 위 링크 참고
# https://velog.io/@sunkyuj/python-%EB%B0%B1%EC%A4%80-15486-%ED%87%B4%EC%82%AC-2

import sys
input = sys.stdin.readline

days = []
days.append([0,0])
def solution():
    n = int(input())
    for _ in range(n):
        day, pay = list(map(int, input().split()))
        days.append([day,pay])
        
    result_pay =  [0 for _ in range(n+1)]
    
    
    
    # 1일 ~ n일까지 하나씩 진행
    for i in range(1,n+1):
        # 전 날과 현재날짜와 비교해서 최대값을 현재날짜에 삽입
        result_pay[i] = max(result_pay[i] ,result_pay[i-1] )
        
        
        # 상담이 끝나는 날 지정
        # 상담일수는 현재날짜 포함 t 이므로 -1을 추가로 진행
        work_day = i + days[i][0] -1
        
        
        # 상담이 끝나는 날이 최대길이 안에 있을 경우
        # 상담일이 끝나는 날 기준 기존에 있떤 값 vs 앞으로 진행될 합친 값 비교
        if work_day <= n :
            result_pay[work_day] = max(result_pay[work_day], result_pay[i-1]+days[i][1])
            
        # print(result_pay)        
    print(max((result_pay)))

if __name__ == '__main__':
    solution()
    