'''
Date        : 2023.09.19
Problem     : https://school.programmers.co.kr/learn/courses/30/lessons/60057
Tag         : 문자열
'''

def solution(s):

    list_count = []                     # 모든 압축된 문자열 길이를 담은 리스트    
    
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s)//2+1):     # i : 자르는 단위
        count = 0
        prev_ch = ["", 0]                # 비교할 자른 문자
        for j in range(0, len(s), i):   # 문자열 s를 앞에서부터 i개씩 잘라서 확인
            curr_ch = s[j:j+i]
            if curr_ch == prev_ch[0]:      # 이전 단위 문자열과 현재 단위 문자열이 동일하다면
                prev_ch[1] += 1           # 이전 동일한 문자열의 개수 체크 
                # if prev_ch[1] == 2:          # 이전 동일한 문자열이 1개였다면 
                #     count += len(str(prev_ch[1]))             # 숫자 길이 추가 
                if j+i >= len(s): # 마지막 단위 문자일 때 
                    count += len(str(prev_ch[1])) 
            else:
                if prev_ch[1] > 1:
                    count += len(str(prev_ch[1]))  # 숫자 길이 추가 
                prev_ch[0] = curr_ch      # 현재 단위 문자로 바꾸기
                prev_ch[1] = 1
                count += len(curr_ch)    
            # print(prev_ch[0], curr_ch, count)   
        list_count.append(count)
        # print(i,'개:', count)
    return min(list_count)