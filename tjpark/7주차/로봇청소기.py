#13:40

import sys

r, c = map(int,sys.stdin.readline().split())

y, x, d = map(int,sys.stdin.readline().split())

board = [list(map(int,sys.stdin.readline().split())) for _ in range(r)]

# 1.현재 칸 청소
# 2.주변 4칸 중 청소 필요없는 경우
# 바라보는 방향을 유지한 채로 한 칸 후진 후 벽이면 작동 멈춤
# 3. 4칸 중 청소 필요한 칸 있는 경우
# 반시계 방향으로 회전, 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진

# 청소한 구역 카운트
result = 0

while(1):
    # 이동 시 벽인 경우
    if board[y][x] == 1:
        break
    
    # 현재 칸 청소안한 경우 청소
    if board[y][x] == 0:
        board[y][x] = 2
        result += 1
    
    # 바라보는 방향에 따른 회전 방향 정해주기
    if d == 0: # 북쪽
        direct = [(0,-1),(1,0),(0,1),(-1,0)]
    elif d == 1: # 동쪽
        direct = [(-1,0),(0,-1),(1,0),(0,1)]
    elif d == 2: # 남쪽
        direct = [(0,1),(-1,0),(0,-1),(1,0)]
    else: # 서쪽
        direct = [(1,0),(0,1),(-1,0),(0,-1)]

    # 반시계 방향 회전하며 이동 방향 정하기
    md = d
    for dy,dx in direct:
        md -= 1
        if md < 0:
            md = 3
        my = y + dy
        mx = x + dx
        if board[my][mx] == 0:
            x = mx
            y = my
            d = md
            break

    # 청소 안된곳 없다면 방향 유지하면서 후진
    else:
        my, mx = direct[-1]
        y += my * -1
        x += mx * -1
    
print(result)





