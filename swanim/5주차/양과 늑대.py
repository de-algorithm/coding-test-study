def solution(info, edges):
    answer = []
    visited = [False] * len(info)

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else: return
        
        for parent, child in edges:
            if visited[parent] and not visited[child]:
                visited[child] = True
                if info[child] == 1: # wolf
                    dfs(sheep, wolf + 1)
                else: # sheep
                    dfs(sheep + 1, wolf)
                visited[child] = False
    
    visited[0] = True
    dfs(1,0)
    return max(answer)