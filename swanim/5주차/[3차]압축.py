def solution(msg):
    answer = []
    dic = {}
    
    for i in range(26):
        dic[chr(65 + i)] = i + 1
    
    i = j = 0
    while True:
        j += 1
        if len(msg) == j : #
            answer.append(dic[msg[i:j]])
            break
        
        if msg[i:j+1] not in dic:
            dic[msg[i:j+1]] = len(dic) + 1
            answer.append(dic[msg[i:j]])
            i = j
        
    return answer