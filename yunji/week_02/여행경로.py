from collections import defaultdict 
def solution(tickets):
    answer = []
    dic = defaultdict(list)
    
    for ticket in tickets:
        dic[ticket[0]].append(ticket[1]) 
        
    for k, v in dic.items():
        v.sort(reverse=True)    # value인 list에서 가장 뒤에 있는 요소가 pop되기 때문에

    stack = ["ICN"]

    while stack:
        top = stack.pop()
        if top not in dic or not dic[top]:
            answer.append(top)
        else:
            stack.append(top)
            stack.append(dic[top].pop())
    
    return answer[::-1]