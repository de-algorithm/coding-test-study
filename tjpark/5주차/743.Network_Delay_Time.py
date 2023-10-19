# n = node개수, times = 엣지간 도달 시간 (u=출발지, v=도착지, w=시간)
# k번 node에서 시작할 때 모든 노드에 도달하는 최소시간을 반환
# 불가능할경우 -1 반환

# n개의 node를 들르는지 체크
# 시간초를 세려면 같은 곳에서 뻣어 나가는것 부터 체크
# 그러려면 딕셔너리로 연결된 노드들을 저장하고, 엣지에 도달하는 최소시간을 비교해 넣기
# {Node_n :{node_n:time, }}

# 48번 케이스 타임초과 ㅠ
# 왜 뜨는지 모르겠음
from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        node_dic = dict()
        time_dic = { i+1:6001 for i in range(n)}
        time_dic[k] = 0
        visited = [[0]*n for _ in range(n)]
        que = deque()
        for u,v,w in times:
            if u not in node_dic:
                node_dic[u] = {v : w}
            else:
                if v not in node_dic[u]:
                    node_dic[u][v] = w
        
        if n == 1:
            return 0
        elif k not in node_dic and n>=2:
            return -1
        else:
            for n, t in list(node_dic[k].items()):
                que.append([k,n,t])

        # 1. k부터 시작해 k안에 있는 사전 순회
        # 2. 순회하면서 엣지에 도달하는 최소 시간 계산하며 dic에 저장
        # 3. 최소시간이 가장 큰 값 = 모든 노드를 돌았을 때 최소 시간
        while que:

            curr, next_node, time = que.popleft()
            
            # 현재 노드까지의 시간 + 다음 노드까지의 걸리는 시간
            cal_time = time_dic[curr] + time
            
            # 다음 노드의 최솟값을 계산
            if time_dic[next_node] > cal_time:
                time_dic[next_node] = cal_time

            visited[curr-1][next_node-1] = 1 
            # 다음 노드에서 갈 수 있는 후보군 que에 넣기
            if next_node in node_dic:
                for n, t in list(node_dic[next_node].items()):
                    if visited[next_node-1][n-1]== 0:
                        que.append([next_node, n, t])
            
        
        max_time = max(time_dic.values())

        if max_time == 6001:
            return -1
        else:
            return max_time 


