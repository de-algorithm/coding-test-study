# start : 12 : 00
# end : 15:30



# 두번째로 시도한 방법
# 13 : 13 ~ 15:30
"""
접근을 dict로 해보자
출발지, 도착지 로 일정하게 나타나니깐
출발지를 Key로 주고도착지를 Value로 준다면?

2번을 예시로 들어본다면 ( dict 후 sort 까지 한 결과 )
#### 실제로는 pop을 사용해야해서 내림차순 정리로 진행! ####

[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
=> 
ATL : ICN, SFO
ICN : ATL, SFO
SFO : ATL

이런식으로 정리가 될 것이다.


알파뱃순으로 넣는다면 
[ ICN > ATL > ICN > SFO > ATL > SFO ] 끝이난다

# 근데 만약 알파뱃 순으로 했는데 끝이 다르게 나타난다면?

ICN : A B
B : ICN

[ ICN > A ... ] 끝

그 후 알파벳 순으로 넣는데, 그 다음 경로가 없을 때를 대비하여 check_list를 하나 만든다
check_list = []

>>>>
1. 비교는 항상 check_list의 맨 끝 값으로 한다
2. 비교를 해서 끝 값에 해당하는 dict value가 있으면 check_list에 넣는다.
 2번 결과 : [ ICN ] 에서 [ ICN, A ]가 된다.
3. 만약 비교했을 때 dict value가 없으면 check_list의 끝 값을 result에 넣는다.
 3번 결과 : 2번에서 check_list는 [ icn ] 이 되고 result에는 [ A ]가 된다.
4. 2번과 3번을 반복한다
 4번 결과 :  3번 이후 1차  >> 
                check_list : [ ICN, B ]
                result : [ A ]
            3번 이후 2차
                check_list : [ ICN, B, ICN ]
                result : [ A ]
            3번 이후 3차 
                check_list : [ ICN, B ]
                result : [ A, ICN ]
            3번 이후 4차
                check_list : [ ICN ]
                result : [ A, ICN, B ]
            3번 이후 5차
                check_list : []
                result : [ A, ICN, B , ICN]
                
            끝




"""




from collections import defaultdict

def solution(tickets):
    # 결과를 넣을 answer 생성
    answer = []
    
    # 리스트 배열의 [0],[1] 을 기준으로 정렬
    # 아래에서 정렬된 dict에서 pop을 사용해야하기때문에 내림차순 정렬로 해야 한다.
    tickets.sort(key = lambda x : (x[0], x[1]), reverse = True)
    
    # dict 생성
    result = defaultdict(list)
    
    
    # defaultdict에 정렬된 순서대로 append
    for key,value in tickets :
        result[key].append(value)

    # 2번 예시 defaultdict(<class 'list'>, {
    #   'ATL': ['ICN', 'SFO'], 
    #   'ICN': ['ATL', 'SFO'], 
    #   'SFO': ['ATL']
    # )
    
    check_list = ["ICN"]
    count = 0
    print(result)
    # print(answer)
    while check_list :
        # 비교할 값이 dict 자체에 없을 때에는 answer에 비교할 값을 append 
        if check_list[-1] not in result or len(result[check_list[-1]]) == 0:
            # print('No!!!!!!')
            answer.append(check_list.pop())
        # 비교할 값이 dict에 있을 때에는 check_list로 가져오기
        else :
            # print('Yes!')
            check_list.append(result[check_list[-1]].pop())
#         print("result :", result)
#         print("answer : ", answer)
#         print("check_list : ",check_list)
    
    

    return answer[::-1]
            
        
    
    

    
    
    



# 알게 된 점
# 파이썬 기본 dict에서는 append가 먹히지 않는다!
## -> 해결방법
## -> from collections imnport defaultfict 를 사용하자




##      ------------------
# 처음 시도한 방법. 근데 뭔가 엄청 복잡해질거같아서 포기
# 13:21 ~ 13:43
# """
# # 1. 시작은 무조건 ICN 이다
#  -> 첫번째 값이 ICN인것 중 알파벳 순으로 정리해서 찾아야한다
#     - tickets.sort(key = lambda x : (x[0], x[1]))
    
#     - answer.append("ICN")
 
# # 2. result = deque(tickets) 에 값이 남지 않을때까지 반복문을 돌면서 일치하는 값을 찾아 answer에 append 한다
# """
# from collections import deque
# def solution(tickets):
#     answer = []
#     # 1
#     tickets.sort(key = lambda x : (x[0], x[1]))
#     answer.append("ICN")
#     print(tickets)
#     print(answer)
    
    
#     result = deque(tickets)
    
#     while result :
        
