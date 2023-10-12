n, m = map(int, input().split())
ls = list(map(int, input().split()))

start, end = 0, max(ls)

while start <= end:
    mid = (start + end) // 2

    tmp = 0
    for i in ls:
        if mid < i:
            tmp += i - mid
    
    if tmp < m:
        end = mid - 1
    else: # tmp >= m
        start = mid + 1

print(end)