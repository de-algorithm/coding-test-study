# 뱀 | Gold 4
# 푼 시간 : 40 h


# 메모리 : 34096 kb
# 시간 : 68 ms


# 첨부된 pdf 참고

# body는 현재 뱀의 위치를 나타냄


# 우선순위
# 1. 일단 움직인다.
# -> body.append(움직인 위치)
# -> count += 1
#  -> 움직인 후 몸 또는 벽이면 break

# 2-1. 움직이기에 성공 후 사과가 없는 자리라면
# -> Body 에 popleft 

# 2-2. 움직이기에 성공 후 사과가 있는 자리라면
# -> continue



import sys
from collections import deque
input = sys.stdin.readline


def sol():
    # 첫째 줄에 보드의 크기 N이 주어진다
    N = int(input())
    board = [[0]*N for _ in range(N)]

    # 다음 줄에 사과의 개수 K가 주어진다
    K = int(input())
    
    
    # 다음 K개의 줄에는 사과의 위치가 주어지
    
    for _ in range(K):
        x,y = map(int,input().split())
        board[x-1][y-1] = 1 
    
    # L개의 줄에는 뱀의 방향 변환 정보가 주어지
    L = int(input())
    order = {}
    for _ in range(L):
        a,b = map(str,input().split())
        # a,b 를 str로 분리했기에 아래에서 편하게 사용하기위해 int(a)로 선언하여 저장
        order[int(a)] = b
        
    # print(order)
    
    # 한가지 방향 ( 오른쪽 )으로 회전
    trun = [[0, 1], [1, 0], [0, -1], [-1, 0]] 
    
    # 현재 오른쪽을 바라보고 있기 때문에 0 
    d = 0 
    
    time = 0
    body = deque([])
    nx = 0
    ny = 0
    
    body.append([0,0])
    while True :
        nx = nx + trun[d][0]
        ny = ny + trun[d][1]
        time += 1
        
        # print(nx, ny)
        # 벽과 닿았거나, 몸통박치기를 했을 경우
        if nx >= N or ny >= N or nx < 0 or ny < 0 or [ nx, ny ] in body :
            break
        
        if board[nx][ny] == 1 :
            board[nx][ny] = 0
        else :
            body.popleft()
        
        body.append( [ nx, ny ])
        # print(body)
        
        if time in order.keys():
            if order[time] == 'L':
                d -= 1
            else :
                d += 1
            
            if d >= 4 :
                d -= 4
            elif d < 0 :
                d += 4
    
    print(time)


if __name__ == '__main__' :
    sol()