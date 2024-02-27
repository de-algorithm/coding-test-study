'''
Date        : 2023.10.11
Problem     : https://school.programmers.co.kr/learn/courses/30/lessons/17680
Tag         : 구현
'''

from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)
    
    if cacheSize == 0:              # 캐시 사이즈가 0일 경우 
        return len(cities) * 5
        
    for city in cities:
        city = city.lower()
        if city in cache:           # cache hit
            cache.remove(city)      
            cache.append(city)
            answer += 1
        else:                       # cache miss
            cache.append(city)
            answer += 5
    return answer