'''
17071.숨바꼭질 5
<문제>
위치가 x일 때 
수빈은 1초에 (x+1, x-1, 2*x) 이동 가능
동생은 매초 +1씩 가속이 붙음 

<입력>
N (int) : 수빈의 위치 (0<= N <= 500,000)
K (int) : 동생의 위치 (0 <= K <= 500,000)

<출력>
int : 수빈이가 동생을 찾는 가장 빠른 시간 
-> 동생을 찾을 수 없거나 찾는 위치가 500,000을 넘을 경우에는 -1

<풀이>

매초마다 
	수빈은 x-1, x+1, 2*x 위치로 bfs 
	동생은 이전 위치 +1로 이동 
		위치가 500,000을 넘으면 -1 반환 

<반례>
34 0
8

27297 339652 
425

4040 160532
385
'''

import sys
from collections import deque

def bfs(N):
    q = deque()
    q.append((N, 0))
    visited[N][0] = 0

    while q:
        for _ in range(len(q)):
            x, t= q.popleft()
            for nx in (x-1, x+1, 2*x):
                if 0 <= nx <= 500000 and visited[nx][(t+1)%2] == -1:
                    q.append((nx, t+1))
                    visited[nx][(t+1)%2] = t+1
                    
                    
N, K = map(int, sys.stdin.readline().split())
visited = [[-1, -1] for _ in range(500001)]


bfs(N)
t = 0
answer = -1

for i in range(500001):
    K += i
    if K > 500000:
        break
    if visited[K][t%2] <= t:
        answer = t
        break
    t += 1

print(answer)