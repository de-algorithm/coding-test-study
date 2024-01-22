#2668번 숫자고르기 | 골드5


# 1 | 2 | 3 | 4 | 5 | 6 | 7
# 3 | 1 | 1 | 5 | 5 | 4 | 6

# # 도착지 dict

# # 1 : 2, 3
# # 2 : x
# # 3 : 1
# # 4 : 6
# # 5 : 5
# # 6 : 7
# # 7 : x










"""


from collections import defaultdict

def dfs(now, start):
    global visited, dict_list, answer
    visited[now] = 1
    
    for n in dict_list[now]:
        if not visited[n]:
            dfs(n,start)
        elif visited[n] and n ==start:
            answer.append(n)


def solution():
    global visited, dict_list, answer
    n = int(input())
    dict_list = defaultdict(list)
    for i in range(1, n+1) :
        dict_list[i].append(int(input()))
        
    answer = []
    
    for i in range(1, n+1):
        visited = [0 for _ in range(n+1)]
        dfs(i,i)
    
    print(len(answer))
    
    for i in range(len(answer)):
        print(answer[i])
        
        
        
if __name__ == '__main__' :
    solution()
    
    
"""