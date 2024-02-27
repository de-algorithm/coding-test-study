from collections import deque


def solution(maps):
    # 상하좌우 움직임
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))  # 큐에 삽입 방문처리는 음..필요없음
        while queue:  # 큐가 존재하는 동안 반복
            x, y = queue.popleft()  # 꺼낸다음에
            for i in range(4):  # 상하좌우 움직여보기
                nx = x + dx[i]
                ny = y + dy[i]
                if (
                    0 > nx or 0 > ny or nx >= len(maps) or ny >= len(maps[0])
                ):  # 범위를 벗어난 경우
                    continue
                if maps[nx][ny] == 0:  # 벽인경우
                    continue
                if maps[nx][ny] == 1:  # 길이 있고 위 조건에 해당하지 않는 경우
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1  # 방문처리 동시에 갱신!

    bfs(0, 0)
    answer = maps[len(maps) - 1][len(maps[0]) - 1]

    if answer == 1:  # 도달할 수 없는 경우
        answer = -1
    return answer
