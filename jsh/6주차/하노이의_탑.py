# 이론은 알겠는데 재귀 구현에서 뭔가 이해가 안가서 다른사람의 풀이를 보고 풀음
# https://mgyo.tistory.com/185#google_vignette
"""
1개일 때
# 1-1
1 > 3으로 이동
 = 1

2개일 때
# 2-1 1번 탑에서 1번째 판 2번 탑으로 이동
# 2-2 1번 탑에서 2번째 판 3번 탑으로 이동
# 2-3 2번 탑에서 1번째 판 3번 탑으로 이동 
=> n=1일 경우 3번 반복

3개일 때
# 3-1. 1번 탑에서 1,2번째 판 2번 탑으로 이동 => n=2일 경우
# 3-2. 1번 탑에서 3번 판 3번 탑으로 이동 => n=1일 경우
# 3-3. 2번 탑에서 1,2번째 판 3번 탑으로 이동 => n=2일 경우
"""

def sol(n, start, end, mid):
    # print(n, start, end, mid)
    global answer
    
    # 3-2 진행
    if n == 1 :
        answer.append([start, end])
    # 2개일 때를 진행
    else :
        # 3-1 진행. 
        # 맨 아래에 있는 애를 end에 보내기위해 다른 나머지를 2번 탑에 쌓기
        sol(n-1,start,mid,end)
        
        answer.append([start,end])
        # 3-3 진행
        sol(n-1,mid,end,start)
    # print(f'3 - end : {answer}')

def solution(n):
    global answer
    answer = []
    sol(n,1,3,2)
    
    return answer


if __name__ == '__main__':
    solution(4)