# 사전에 있으면 출력, 없으면 사전에 추가
# 1. 입력한 값을 사전에 없을 때 까지 계속 더함
# 2. 사전에 있으면 answer에 추가
# 3. 사전에 없으면 있는곳까지 answer에 추가 후 없는 문자 사전에 추가
def solution(msg):
    answer = []
    
    # 초기 사전 설정
    dic = dict()
    for n in range(26):
        tmp = chr(ord('A')+n)
        dic[tmp] = n+1
    
    dic_num = 26
    string = ''
    for w in msg:
        
        string += w
        # 사전에 단어가 없을 경우
        if string not in dic:
            
            # 사전에 없기 전까지의 단어 추출
            s_len = len(string)
            prev_string = string[:s_len-1]

            answer.append(dic[prev_string])
            
            # 사전에 없는 값 추가
            dic_num += 1
            dic[string] = dic_num
            
            string = w
    
    # 마지막 문자 처리
    if string in dic:
        answer.append(dic[string])
    else:
        answer.append(dic_num+1)
    #print(dic)

            
    return answer