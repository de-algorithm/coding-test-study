'''
Date        : 2023.10.18
Problem     : https://school.programmers.co.kr/learn/courses/30/lessons/17684
Tag         : 구현
'''

from collections import defaultdict
def solution(msg):
    answer = []
    index = 1
    
    # 1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
    # {'A': 1, 'B': 2, 'C': 3,...,'Z':26}
    d = defaultdict(int)
    word = 65
    for index in range(index, 27):
        d[chr(word)] = index
        word += 1
    
    # index는 26
    #2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
    w = ""                      # 현재 글자 w
    c_idx = 0                   # 다음 글자 인덱스
    c = ""                      # 다음 글자 c
    j = 0
    n = 0
    flag = False
    for _ in range(len(msg)):       # i: 현재 입력 시작 인덱스 
        i = c_idx
        for j in range(i+1, len(msg)+1):
    
            if d[msg[i:j]] > 0:     # 사전에 등록되어 있다면
                w = msg[i:j]
                output = d[w]
                
                if j == len(msg): # 마지막 입력일 때
                    answer.append(output)   # 출력
                    flag = True
                    break
            else:
                # print("현재 입력(w): ", w)
                answer.append(output)   # 출력
                c_idx = j-1
                c = msg[c_idx]
                
                
                if d[w+c] == 0:        # w+c가 사전에 등록되어 있지 않다면 
                    index += 1
                    d[w+c] = index      # 사전 추가 
                    # print("사전 추가", index,":",w+c)
                break
        if flag:
            break
                
    return answer