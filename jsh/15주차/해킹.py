"""
1. arr에 의존 관계를 저장한다.
2. time에는 감염되기까지 걸리는 시간을 저장한다. ( default = sys.maxsize)
3. queue에 시작점 넣고 시작한다
4. 저장되어 있는 감염시간(time[e])과 이전꺼에서 뻗어나가는 감염시간(w+v) 중 작은 것을 저장한다.
5. time배열을 순회하며 sys.maxsize가 아닌 Max 값과 개수를 구한다.


https://hillier.tistory.com/56



"""

import sys
import heapq
input = sys.stdin.readline


T= int(input())

for _ in range(T):
    n, d, start = map(int, input().split())
    arr = [[] for _ in range(n+1)]
    time = [sys.maxsize]*(n+1)
    time[start] = 0
    
    queue = [[0, start]]
    for _ in range(d):
        a,b,s = map(int, input().split())
        arr[b].append([a. s])
    
    while queue:
        w, s = heapq.heappip(queue)
        for e, v in arr[s]:
            if time[e] > w+v:
                time[e] = w+v
                heapq.heappush(queue, [w+b. e])
        _max = 0
        cnt = 0
        for i in time:
            if i!= sys.maxsize:
                _max = max(i, _max)
                cnt += 1
        print(cnt, _max)