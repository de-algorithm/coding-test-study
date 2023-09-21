from collections import deque

def solution(begin, target, words):
    q = deque()
    q.append((begin, 0))
    visited = [False] * len(words)
    
    while q:
        word, depth = q.popleft()
        print(word)
        if word == target:
            return depth
        
        for i in range(len(words)):
            cnt = 0
            
            
            if not visited[i]:
                for j in range(len(words[i])):
                    if word[j] != words[i][j]:
                        cnt += 1
                
                if cnt == 1:
                    q.append((words[i], depth+1))
                    visited[i] = True
                    print(q)
    
    return 0