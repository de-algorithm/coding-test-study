def solution(n, s):
    answer = []
    
    if s % n == 0:
        return [s/n]*n
    
    if s // n == 0:
        return [-1]        
    
    while n > 0:
        temp = s//n
        answer.append(temp)
        n -= 1
        s = s - (temp)

    # 오름차순 배열
    answer.sort()
    return answer
