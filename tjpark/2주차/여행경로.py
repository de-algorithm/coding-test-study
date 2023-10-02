# 주어진 항공권을 모두 사용해 방문 경로를 return
# 방문 가능 경로 2개 이상 시 알파벳 내림차순으로 return
# 순서대로 갔으나 경로가 존재하지 않을 시 되돌아 와야함
def dfs(tickets_dic, stack, path):
    if not stack:
        path.reverse()
        return path

    depart = stack[-1]

    # 출발지에 해당하는 티켓 있는지 확인
    if depart in tickets_dic and tickets_dic[depart]:
        # 도착지를 스택에 저장
        arrive = tickets_dic[depart].pop()
        stack.append(arrive)
    else:
        # 티켓이 없을 경우
        # 1. 해당 장소에서 출발하는 티켓이 없는 경우
        # 2. 출발하는 티켓은 존재하나 모두 소진한 경우
        no_ticket = stack.pop()
        path.append(no_ticket)
        
    return dfs(tickets_dic, stack, path)

def solution(tickets):

    tickets_dic = {}
    
    # 출발지, 도착지 dict 생성
    for depart, arrive in tickets:
        if depart in tickets_dic: 
            tickets_dic[depart].append(arrive)
        else:    
            tickets_dic[depart] = [arrive]
    
    # pop할 때 알파벳 낮은것 부터 나오도록 정렬
    for k in tickets_dic:
        tickets_dic[k].sort(reverse=True)
    
    print(tickets_dic)
    
    answer = dfs(tickets_dic, ['ICN'], [])
    
    return answer
