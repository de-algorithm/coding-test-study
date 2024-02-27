def solution(s):
    answer = int(1e9)
    end = len(s) + 1
    
    for i in range(1, end//2+1):
        tmp = s[:i]
        cnt, result = 1, ''
        for j in range(i, end+i, i):
            if tmp == s[j:i+j]:
                cnt += 1
                
            else:
                if cnt >= 2:
                    result += str(cnt) + tmp
                    
                else:
                    result += tmp
                tmp = s[j:i+j]
                cnt = 1    

        answer = min(answer, len(result))

    return answer