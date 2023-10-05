def solution(tickets):
    answer = []
    #for i in range(len(tickets)): # 방문체크용 배열 추가
    #    tickets[i].append(False)
    visited = [False] * len(tickets)
    
    def dfs(start, depth, ans):
        if depth == len(tickets):
            answer.append(ans+[start])
            return
        for idx, info in enumerate(tickets):
            if not visited[idx] and start == info[0]:
                visited[idx] = True
                dfs(info[1], depth+1, ans+[info[0]])
                visited[idx] = False
    dfs('ICN', 0, [])
    
    answer.sort()
    result = answer[0]
    
    return result