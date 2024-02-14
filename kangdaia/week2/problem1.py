def solution(tickets: list[list[str]]) -> list[str]:
    """ 프로그래머스 여행경로
    주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.
    항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때,
    방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

    1. 2차원 배열 tickets을 dict 형태로 바꿈
        - 시작하는 공항을 key로, 도착하는 공항을 value list에 담음
            (시작하는 공항 하나에 도착하는 공항이 여러개일 수 있다.)
        - 이후 value list를 리버스로 정렬 (last pop)
    2. stack과 path init
        - stack에 시작 공항인 ICN을 담아 두기
        - path 는 empty list
        - 이후 마지막 스택을 항공권 dict key로 values를 찾아 path에 추가함
    3. backtracking
        - stack이 빌때까지, 마지막 스택을 key로 사용해 routes value 검색
        - 만약 routes value가 없으면 path에 마지막 스택을 넣고 stack에서는 pop
        - 있는 경우, stack에 values list를 pop 해서 stack에 넣음.
        - while loop end
            - path를 reverse해서 return

    Args:
        tickets (list[list[str]]): 항공권 정보가 담긴 2차원 배열 tickets

    Returns:
        list[str]: "ICN" 공항에서 출발해 방문하는 공항 경로
    """
    routes = dict()
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for dep in routes:
        routes[dep] = sorted(routes[dep], reverse=True)
    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]  # else 케이스는 stack pop을 하지 않음.
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop())
    return path[::-1]
