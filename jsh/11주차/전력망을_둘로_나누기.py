# 하나마다 끊어서 이어지는개수를 세어본다
# 40min
#

from collections import defaultdict

def dfs(start, visit):
    global cnt
    visit.append(start)
    cnt += 1
    
    for i in all_dict[start]:
        if i not in visit :
            dfs(i, visit)
            
    
def solution(n, wires):
    global all_dict, cnt
    answer = 1e9
    
    all_dict = defaultdict(list)
    
    for x,y in wires :
        all_dict[x].append(y)
        all_dict[y].append(x)
        
    # print('dict : ',all_dict[1])    
    for x,y in wires :
        # 연결점 끊기
        all_dict[x].remove(y)
        all_dict[y].remove(x)
        
        cnt = 0
        dfs(1,[])
        
        answer = min(answer, abs(n-(cnt*2)))
        
        all_dict[x].append(y)
        all_dict[y].append(x)
    
    
    return answer