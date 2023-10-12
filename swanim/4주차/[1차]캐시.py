from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    for i in cities:
        i = i.upper() 
        if i in cache:
            cache.remove(i)
            cache.appendleft(i)
            answer += 1 # hit
        else:
            if len(cache) == cacheSize and cacheSize != 0:
                cache.pop()
            if cacheSize == 0: 
                return len(cities) * 5
            cache.appendleft(i)
            answer += 5 # miss
    return answer