# problem : https://www.acmicpc.net/problem/1600

import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(H)]


horse = [(-2,-1), (-2, 1), (-1, 2), (-1,-2), (1, -2), (1, 2), (2, -1), (2, 1)]
monkey = [(1, 0),(-1, 0), (0, 1), (0, -1)]
def bfs():
    q = deque()
    visited = [[-1 for _ in range(W)] for _ in range(H)]
    q.append((0,0,K))
    visited[0][0] = 0
    
    while q:
        x, y, k = q.popleft()
        if k > 0:
            for dx, dy in horse:
                nx, ny = x+dx, y+dy
                if 0 <= nx < H and 0 <= ny < W:
                    if visited[nx][ny] == -1 and map[nx][ny] == 0:
                        q.append((nx, ny, k-1))
                        print("horse:",(nx, ny, k-1))
                        visited[nx][ny] = visited[x][y] + 1
        for dx, dy in monkey:
            nx, ny = x+dx, y+dy
            if 0 <= nx < H and 0 <= ny < W:
                if visited[nx][ny] == -1 and map[nx][ny] == 0:
                    q.append((nx, ny, k))
                    print("monkey:",(nx, ny, k))
                    visited[nx][ny] = visited[x][y] + 1
    return visited[H-1][W-1]


print(bfs())