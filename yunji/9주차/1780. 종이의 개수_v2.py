import sys
sys.stdin = open('yunji/input.txt', 'r')
input = sys.stdin.readline

N = int(input())
array = [list(map(int, input().strip().split(' '))) for _ in range(N)]


answer = [0, 0, 0]

def dfs(N, x, y):
    tmp = array[x][y]
    
    if N == 1:
        answer[tmp+1] += 1
        return

    for i in range(x, x+N):
        for j in range(y, y+N):
            if array[i][j] != array[x][y]:
                for a in range(x, x+N, N//3):
                    for b in range(y, y+N, N//3):
                        dfs(N//3, a, b)

                return
    
    answer[tmp+1] += 1

dfs(N, 0, 0)

print('\n'.join(map(str, answer)))