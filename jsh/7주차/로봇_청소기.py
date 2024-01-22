# 14503 로봇 청소기 | 골드 5
# https://www.acmicpc.net/problem/14503

"""
1순위 : 현재 해당 방이 청소되었는지 ( 맨 처음만 )

2순위 : 바라보는 시점기준 반시계 방향으로 돌고 비교 후 청소할 곳이 있으면 이동

3순위 : 상하좌우 비교 후 다 청소되었으면 후진




"""

#반시계로 돌아가기
def left():
    global d
    d -= 1
    if d == -1:
        d = 3



def solution():
    global d
    
    n, m = map(int, input().split())
    #좌표값, 방향
    x, y, d = map(int, input().split())

    # 청소했는지 안했는지 체크하기위한 배열
    check = [[0]*m for _ in range(n)]

    # 방 가져오기
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    #동서남북 
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

# 1순위 : 현재 해당 방이 청소되었는지
    # 로봇 청소기가 있는 칸은 항상 빈 칸이다. 
    check[x][y] = 1
    count = 1
    turn = 0


    while True:
#  2순위 : 바라보는 시점기준 반시계 방향으로 돌고 비교 후 청소할 곳이 있으면 이동
        left()
        # 비교할 위치 좌표 
        nx = x + dx[d]
        ny = y + dy[d]
        #청소하지 않은 공간이 존재한다면 청소 후 += 1
        if check[nx][ny] == 0 and arr[nx][ny] == 0:
            check[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn = 0
            continue
        else:
            turn += 1

        #네 방향 모두 청소 or 벽
        if turn == 4:
            # 후진할 좌표 지정
            nx = x - dx[d]
            ny = y - dy[d]
            # 후진할 곳이 있으면 후진
            if arr[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn = 0

    print(count)



if __name__ == '__main__':
    solution()