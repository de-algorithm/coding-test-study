'''
Date        : 2023.09.21
Problem     : https://school.programmers.co.kr/learn/courses/30/lessons/60061
Tag         : 구현
'''

def solution(n, build_frame):
    answer = []
    
    for info in build_frame:
        x, y, a, b = info
        
        # # 삭제일 때
        if b == 0:                  
            answer.remove([x,y,a])  # 해당 구조물 삭제
            if check(answer):       # 삭제 가능한지 판단 
                continue
            answer.append([x,y,a])
        # 설치일 때
        if b == 1:   
            answer.append([x,y,a])  # 해당 구조물 설치
            if check(answer):       # 설치 가능한지 판단
                continue
            answer.remove([x,y,a])
            
    return sorted(answer)

# 기둥과 보의 설치 가능 여부
def check(answer):
    for x,y,a in answer:
        # 기둥일 때
        if a == 0:
        # 기둥이 바닥 위 or 다른 기둥 위 or 보의 한쪽 끝 
            if y == 0 or [x,y-1,0] in answer or [x,y,1] in answer or [x-1,y,1] in answer:
                continue
            return False
        # 보일 때
        else:
            # 보의 한쪽 끝이 기둥 위 or 양쪽 끝이 동시에 다른 보에 연결
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True