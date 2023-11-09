import sys
from collections import deque

sys_input = sys.stdin.readline

N = int(sys_input())
K = int(sys_input())

board = [[0] * N for _ in range(N)]

for _ in range(K):
    y, x = map(int,sys_input().split())
    board[y-1][x-1] = 2

L = int(sys_input())

direct = deque([sys_input().split() for _ in range(L)])

# 뱀이 벽이나 자신의 몸과 부딪히면 끝
# 사과가 있다면, 사과가 없어지고 꼬리 그대로
# 사과 없다면, 전체 이동
# 몇 초에 끝나는지 출력
time = -1
hy, hx = (0,0)

# 상, 우, 하, 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
d = 1

tail = deque([])

while(1):
    time += 1

    # 벽 또는 자기 몸에 부딪혔을 때
    if hy < 0 or hy >= N or hx < 0 or hx >= N \
        or board[hy][hx] == 1:
        print(time)
        break

    # 사과가 있을 경우
    elif board[hy][hx] == 2:
        board[hy][hx] = 1
        # 꼬리 추가
        tail.append((hy,hx))
    
    # 사과가 없을 경우
    else:
        # 꼬리 움직이기
        tail.append((hy,hx))
        board[hy][hx] = 1
        if len(tail) > 1:
            ty, tx = tail.popleft()
            board[ty][tx] = 0

    # 다음 진행 방향 설정
    if direct and int(direct[0][0]) == time:
        _, turn = direct.popleft()
        if turn == 'D':
            d = (d+1) % 4
        else:
            d = (d+4-1) % 4
    
    # print(time, hy, hx)
    # print(board)
    
    # 다음 진행 방향으로 머리 움직이기
    my = hy + dy[d]
    mx = hx + dx[d]
    hy, hx= my, mx

