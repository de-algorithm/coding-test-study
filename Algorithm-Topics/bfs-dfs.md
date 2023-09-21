# dfs / bfs

<br>

## DFS (Depth-First Search)

- 깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색

→ 한 방향으로 모든 노드를 방문하다 더 이상 다른 노드를 방문할 수 없을 때 가장 가까운 길로 돌아가 방문하지 않은 노드로 탐색을 이어감

- 스택, 재귀 이용해 구현

### 스택 풀이

```python
def dfs(start_v):
visited =[]
stack = [start_v] # 경로 정보 추적
while stack:
	v = stack.pop()
	if v not in visited:
		visited.append(v)
		for w in graph[v]:
			stack.append(w)
return visited
```

### 재귀 풀이

```python
def recursive_dfs(v, visited=[]):
    visited.append(v)
    for w in graph[v]:
        if not w in visited:
            visited = recursive_dfs(w,visited)
    return visited
```

## BFS (Breadth-first search)

- 그래프에서 시작 노드에 인접한 노드부터 탐색

### 탐색 방법

1. 시작 노드를 큐에 삽입하고 방문 처리
2. 큐에서 노드를 꺼내 방문하지 않은 인접 노드 정보를 큐에 넣고 방문 처리
3. 2번 과정이 종료될 때까지 반복

```python
from collections import deque

def bfs(start_v):
    visited = [start_v]
    deq = deque()
    deq.append(start_v)
    while deq:
        v = deq.popleft()
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                deq.append(w)
    return visited
```
