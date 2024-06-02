# problem : https://www.acmicpc.net/problem/13913

import sys
from collections import deque

def bfs():
    
    q = deque()
    visited = [0 for _ in range(100001)]
    q.append((N, 0, [N]))
    visited[N] = 1
    
    if N > K:
        return N-K, [i for i in range(N, K-1, -1)]

    while q:
        x, t, p = q.popleft()
        if x == K:
            return t, p
        for nx in [x-1, x+1, x*2]:
            if 0 <= nx <= 100000 and visited[nx] == 0:
                q.append((nx, t+1, p+[nx]))
                visited[nx] = 1
    
    
    
# N은 수빈, K는 동생이 있는 위치 
N, K = map(int, sys.stdin.readline().split())

time, path = bfs()
print(time)
print(*path)


