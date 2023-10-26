# 원판이 큰 순서대로 아래부터 쌓여있기 때문에 원판이 2개 이상인 경우
# 보조기둥에 쌓았다가 도착 기둥에 다시 큰 순서대로 쌓아야됨
answer = []
# n = 남은 원반의 개수
# from_p = 출발 기둥 / to_p = 도착 기둥
# sub_p = 보조 기둥
def move(n, from_p, to_p, sub_p):
    global answer
    # print(n, from_p, to_p)
    # 원반 한 개만 옮기면 되는 경우
    if n == 1:
        answer.append([from_p, to_p])
        return
    
    # 원반 n-1개를 sub로 이동(to_p를 보조 기둥으로 사용)
    move(n-1, from_p, sub_p, to_p)
    answer.append([from_p, to_p])
    
    # sub에 있는 원반 n-1개를 목적지로 이동(from_p를 보조 기둥으로 사용)
    move(n-1, sub_p, to_p, from_p)
    
def solution(n):
    global answer
    move(n,1,3,2)
    
    return answer
