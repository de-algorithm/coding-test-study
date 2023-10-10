def solution(stones, k):

    start, end = 1, max(stones)
    while start <= end:
        mid = (start + end) // 2
        
        cnt = 0
        for i in stones:
            if i - mid <= 0:
                cnt += 1
                
                if cnt >= k:
                    break
            else :
                cnt = 0
        
        if cnt >= k:
            end = mid - 1
        else:
            start = mid + 1
    
    return start