'''
1. wires로 트리 생성
2. 전선 한 개씩 삭제 -> BFS로 두 네트워크 노드 개수 계산하며 answer 저장
3. n이 홀수일 때 answer=1, n이 짝수일 때 answer=0이면 바로 return
4. answer 갱신하며 최솟값을 return
'''
from collections import defaultdict
from collections import deque
def solution(n, wires):
    answer = n
    tree = defaultdict(list) 
    for wire in wires:
        tree[wire[0]].append(wire[1])
        tree[wire[1]].append(wire[0])
    
    for i in range(len(wires)):
        # 전선 삭제
        removed_wire = wires[i]
        tree[removed_wire[0]].remove(removed_wire[1])
        tree[removed_wire[1]].remove(removed_wire[0])

        # print(removed_wire , "삭제")
        visited = [False] * (n+1)
        count = bfs(tree, 1, visited)
        # print(count, ",", n-count)
        
        diff = abs(2*count-n)
        answer = min(answer, diff)
        
        # n이 홀수일 땐 최솟값 1, 짝수일 땐 0임 
        # 최솟값 발견시 바로 answer 리턴
        if n % 2 == 0:
            if answer == 0:
                return answer
        else:
            if answer == 1:
                return answer
        
        # 전선 복구
        tree[removed_wire[0]].append(removed_wire[1])
        tree[removed_wire[1]].append(removed_wire[0]) 
        
    return answer
        
def bfs(tree, start, visited):
    
        queue = deque([start])   
        visited[start] = True
        count = 1
    
        while queue:
            n = queue.popleft()
            for j in tree[n]:
                if not visited[j]:
                    queue.append(j)
                    visited[j] = True
                    count += 1
                    
        return count