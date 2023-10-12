# cache hit = 1, miss = 5
# return: 캐시 크기에 따른 실행시간을 측정해라
# 
# 1.캐시 사이즈에 맞는 배열 생성
# 2.도시순서대로 캐시가 쌓일 때 까지 append
# 3.캐시에 해당 데이터가 있는 경우 pop후 append
# 4.캐시가 꽉 찾을 때 해당 데이터가 없는 경우 맨앞pop, append데이터 

from collections import deque
def solution(cacheSize, cities):
    answer = 0
    
    cache_q = deque()
    
    for city in cities:
        # 도시명 모두 소문자로 변경
        city = city.lower()
        
        # 캐시크기가 0일 경우
        if cacheSize == 0:
            answer = len(cities) * 5
            break
        # 캐시에 도시가 이미 있을 경우
        elif city in cache_q:
            # 캐시 맨끝에 있지 않으면 해당 데이터 삭제후 맨끝에 추가
            if cache_q[-1] != city:
                cache_q.remove(city)
                cache_q.append(city)
            answer += 1
        # 캐시에 도시가 없고 공간이 있을 경우 도시 추가
        elif cacheSize > len(cache_q):
            cache_q.append(city)
            answer += 5
        # 캐시에 도시도 없고 공간도 없으면 맨앞 삭제 후 뒤에 도시 추가
        else:
            cache_q.popleft()
            cache_q.append(city)
            answer += 5

        #print(cache_q)
    return answer