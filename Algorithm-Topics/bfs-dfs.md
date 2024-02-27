# dfs / bfs

<br>

## DFS (Depth-First Search)

- 깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색

→ 한 방향으로 모든 노드를 방문하다 더 이상 다른 노드를 방문할 수 없을 때 가장 가까운 길로 돌아가 방문하지 않은 노드로 탐색을 이어감

- 스택, 재귀 이용해 구현

### 스택 풀이

![DFS](https://github.com/de-algorithm/coding-test-study/assets/64563859/5e45ea5a-3d47-4695-94a9-7337bff21a58)

<br>

이미지 출처 : https://velog.io/@himinhee/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-DFS%EA%B9%8A%EC%9D%B4-%EC%9A%B0%EC%84%A0-%ED%83%90%EC%83%89-BFS%EB%84%88%EB%B9%84-%EC%9A%B0%EC%84%A0-%ED%83%90%EC%83%89

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

![img](https://github.com/de-algorithm/coding-test-study/assets/64563859/1a16e855-7e81-47a9-8a3a-ffaade377d70)

<br>

이미지 출처 : https://iq.opengenus.org/dfs-vs-bfs/
