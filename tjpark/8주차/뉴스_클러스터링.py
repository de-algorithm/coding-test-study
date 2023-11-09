# 2개 글자를 묶은 원소를 retrun = (교집합/합집합 * 65536)

from collections import defaultdict

def divide(str_in):
    str_in = str_in.lower()
    result_dic = defaultdict(int)
    
    for i in range(len(str_in)):        
        # 2개씩 자르다가 특수문자 or 기타문자 나오면 넘어가기
        if not str_in[i:i+2].isalpha():
            pass
        elif i < len(str_in)-1:
            result_dic[str_in[i:i+2]] += 1

    return result_dic

def calc(str1_dic_in, str2_dic_in):
    cross_agg = 0 
    sum_agg = 0
    
    for s1_key in str1_dic_in:
        
        for _ in range(str1_dic_in[s1_key]):
            # 교집합 찾기
            if s1_key in str2_dic_in:
                str2_dic_in[s1_key] -= 1
                if str2_dic_in[s1_key] == 0:
                    del str2_dic_in[s1_key]
                cross_agg += 1
            # str1 원소 합집합에 추가
            sum_agg += 1
    
    # str2 원소 합집합에 추가
    sum_agg += sum(str2_dic_in.values())
    
    if str2_dic_in or str1_dic_in:
        result = cross_agg / sum_agg * 65536
    else:
        result = 65536
    
    return int(result)
            
    
    
def solution(str1, str2):

    str1_dic = divide(str1)
    str2_dic = divide(str2)
    
    answer = calc(str1_dic, str2_dic)
    
    return answer