# 전화 종료 시간 계산하기
def time_calc(h, m, d):
    m = m+d   
    if m > 60:
        h += 1
        m -= 60
        if h == 24:
            h = 0
    return h, m

def solution(N, info):
    answer = 0
    
    for ele in info:
        h, m = map(int, ele[:6].split(":"))
        d = int(ele[6:])
        # 전화 요금 계산하기
        end_h, end_m = time_calc(h, m, d)
        
        fare = 0
        # HH:MM이 7:00 ~ 19:00 사이
        if 7 <= h < 19 and m >= 0:   
            # HH:MM 에서 DD를 더했을 때 19:00을 넘는다면
            if end_h >= 19 and end_m >=0:
                fare += ((60-m)*10) + (end_m*5)
            # 안넘는다면
            else:
                fare += (d*10)
        # HH:MM이 19:00 ~ 7:00 사이
        else:
            # HH:MM 에서 DD를 더했을 때 7:00을 넘는다면
            if 7 <= end_h <= 18 and end_m >= 0:
                fare += ((60-m)*5) + (end_m*10)
            # 안넘는다면
            else:
                fare += (d*5)

        answer += fare
    return answer



import sys
N = int(sys.stdin.readline())
info = []
for _ in range(N):
    info.append(sys.stdin.readline())

print(solution(N, info))