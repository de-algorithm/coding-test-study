import sys
from collections import deque

input = sys.stdin.readline
move = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
]

def bfs():
    while q_f:
        x, y = q_f.popleft()

        for i in range(4):
            nx, ny = x + move[i][0], y + move[i][1]

            if 0 <= nx < w and 0 <= ny < h:
                if not visited_f[nx][ny] and graph[nx][ny] != "#":
                    visited_f[nx][ny] = visited_f[x][y] + 1
                    q_f.append((nx, ny))
    
    while q_j:
        x, y = q_j.popleft()

        for i in range(4):
            nx, ny = x + move[i][0], y + move[i][1]

            if 0 <= nx < w and 0 <= ny < h:
                if graph[nx][ny] != "#" and not visited_j[nx][ny]:
                    if not visited_f[nx][ny] or visited_f[nx][ny] > visited_j[x][y] + 1:
                        visited_j[nx][ny] = visited_j[x][y] + 1
                        q_j.append((nx, ny))

            else:
                return visited_j[x][y]

    
    return "IMPOSSIBLE"

answer = []
T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    graph = []
    q_j = deque()
    q_f = deque()

    visited_j = [[0] * h for _ in range(w)]
    visited_f = [[0] * h for _ in range(w)]
    
    for i in range(w):
        temp = list(input().strip())

        for j in range(len(temp)):
            if temp[j] == "@":
                q_j.append((i, j))
                visited_j[i][j] = 1
            
            elif temp[j] == "*":
                q_f.append((i, j))
                visited_f[i][j] = 1
            
        graph.append(temp)
    answer.append(bfs())
for item in answer:
    print(item)