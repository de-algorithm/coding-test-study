import sys
sys.setrecursionlimit(10**5)
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

p = [0, 0, 0]

def dfs(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != paper[x][y]:
                for k in range(3):
                    for l in range(3):
                        dfs(x + k * (n // 3), y + l * (n // 3), n // 3)
                return
    
    p[paper[x][y]+1] += 1

dfs(0, 0, n)
print(*p, sep='\n')