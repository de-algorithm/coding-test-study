from collections import deque

n, m = map(int, input().split())
cmd = [list(map(int, input().split())) for _ in range(m)]
train = [deque([0]*20) for _ in range(n)]

for i in cmd:
    if i[0] == 1:
        train[i[1]-1][i[2]-1] = 1
    elif i[0] == 2:
        train[i[1]-1][i[2]-1] = 0
    elif i[0] == 3:
        train[i[1]-1].rotate(1)
        train[i[1]-1][0] = 0
    else:
        train[i[1]-1].rotate(-1)
        train[i[1]-1][19] = 0

ans = []
for i in train:
    if i not in ans:
        ans.append(i)

print(len(ans))