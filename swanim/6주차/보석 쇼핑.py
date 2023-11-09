def solution(gems):
    answer = [1, len(gems)]
    dic = {gems[0] : 1}
    gems_set = set(gems)
    print(gems_set)
    start = end = 0
    while start <= end < len(gems):
        if len(dic) == len(gems_set): # gems을 다 모았다면
            if answer[1] - answer[0] > end - start:
                answer = [start+1, end+1]
            
            dic[gems[start]] -= 1
            if dic[gems[start]] <= 0:
                del dic[gems[start]]
            start += 1
        
        else:
            end += 1
            if end >= len(gems):
                break
            if gems[end] not in dic:
                dic[gems[end]] = 1
            else:
                dic[gems[end]] += 1
    
    return answer