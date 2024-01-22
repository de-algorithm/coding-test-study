# 구현
# Lv2


# start : 9:04
# end : 10:12
# time : 1h

# 교집합 : intersection 
# 합집합 : union

# 1. 일단 대소문자만 남겨보자 
#  => 정규식 ( re ) + upper 를 사용하여 대/소문자 통합

# 2. 문자열을 두 글자씩 끊어서 list에 보관하자
#  => word = s[i:i+2]  
#     => all_list.append(word)


# 문제에서 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의한다.
### 공집합을 찾는 조건을 걸어놓자
###  => if len(A) == 0 and len(B) == 0: answer = 1
        
# 3. 교집합 합집합을 구하자 
#   => set(A) | set(B) ,    
#   => set(A) & set(B)

# 4. 다중집합은 총 개수를 count해서 min max로 하자




# import re

# def get_list(s):
    
#     s = re.sub(r"[^A-Z]", "", (s.upper()))
    
#     all_list = list()
    
#     for i in range(0,len(s)-1):
#         word = s[i:i+2]
#         all_list.append(word)
#     print(all_list)
#     return all_list


def get_list_v2(s):
    all_list = list()
    s = s.upper()
    for i in range(0,len(s)-1):
        word = s[i:i+2]
        
        if word.isalpha():
            all_list.append(word)
    # print(all_list)
    return all_list
    
    
                        

def solution(str1, str2):
    
    arr_1 = get_list_v2(str1)
    arr_2 = get_list_v2(str2)
    
    
    if len(arr_1) == 0 and len(arr_2) == 0 :
        answer = 1
    
    else :
        inter = set(arr_1) & set(arr_2)
        union = set(arr_1) | set(arr_2)
        # print(inter)
        # print(union)
        all_inter = 0
        all_union = 0

        for i in inter:
            all_inter += min(arr_1.count(i), arr_2.count(i))
            # print(all_inter)

        for i in union:
            all_union += max(arr_1.count(i), arr_2.count(i))
            # print(all_union)

    
        answer = all_inter / all_union
    
    # print(answer)
    # print(int(answer*65536))
        
    
    return int(answer*65536)

