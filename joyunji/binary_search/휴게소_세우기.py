# https://www.acmicpc.net/problem/1477
import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
place = [0]+list(map(int, input().split()))+[L]

answer = 0
place.sort()

l, r = 1, L-1
while l <= r:
    m = (l+r)//2
    count = 0

    for i in range(1, len(place)):
        if place[i] - place[i-1] > m:
            count += ((place[i] - place[i-1]-1)//m)

    if count > M:
        l = m+1
    else:
        answer = m
        r = m-1

print(answer)