# start > 18:00
# end > 18:20
"""
1. 들어오는 순으로 정렬한다
2. 첫 번째 값을 입장 값으로 넣는다.
3. 다음값부터 입장값과 비교해가면서 넘어가는지 안넘어가는지 비교한다.
4. 넘어가면 +1 후 입장값 새로 수정 
5. 끝나면 전체 count 나타내기
"""

def solution(routes):
    answer = 1
    routes.sort(key = lambda x: x[1])
    print(routes)
    check = routes[0][1]
    for i in range(1,len(routes)) :
        if check < routes[i][0]:
            check = routes[i][1]
            answer += 1
    return answer
