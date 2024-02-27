import heapq
from collections import deque
n = int(input())
board = [[0] * n for _ in range(n)]

# 사과 board에 저장
for i in range(int(input())):
    r, c = map(int, input().split())
    board[r-1][c-1] = 2

# 방향 저장
direction_change = []
for i in range(int(input())):
    sec, dir = input().split()
    heapq.heappush(direction_change, (int(sec), dir))

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer_sec = 0
di = 1 
cur_i, cur_j = 0, 0 
board[cur_i][cur_j] = 1 # 뱀 초기 위치
tail_q = deque([(cur_i, cur_j)]) 

while True:
    # 방향 변환
    if len(direction_change) != 0 and direction_change[0][0] == answer_sec:
        x, c = heapq.heappop(direction_change)
        if c == 'L': 
            di = (di + 3) % 4
        else:
            di = (di + 1) % 4 # 
    
    cur_i += dxy[di][0] #
    cur_j += dxy[di][1]
    
    if (0 > cur_i or cur_i >= n or 0 > cur_j or cur_j >= n) or board[cur_i][cur_j] == 1:
        break
    
    if board[cur_i][cur_j] == 2: # 사과 있으면
        board[cur_i][cur_j] = 1
        tail_q.append((cur_i, cur_j))
    else:
        board[cur_i][cur_j] = 1
        
        t_i, t_j = tail_q.popleft()
        board[t_i][t_j] = 0 # 꼬리 이동
        tail_q.append((cur_i, cur_j))

    answer_sec += 1

print(answer_sec+1)