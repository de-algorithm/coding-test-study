n = int(input())
ls = [[] for _ in range(n+1)]
for i in range(1, n+1):
    ls[i].append(int(input()))

ans = []

def dfs(num):
    if visited[num] == False:
        visited[num] = True
        for n in ls[num]:
            set1.add(num)
            set2.add(n)

            if set1 == set2:
                ans.extend(list(set2))
                return
            dfs(n)
    visited[num] = False

for i in range(1, n+1):
    visited = [False] * (n+1)
    #set1 = set2 = set()
    set1 = set()
    set2 = set()

    dfs(i)

ans = list(set(ans))
ans.sort()

print(len(ans))
for n in ans:
    print(n)