# 10:25
# S= 문자열 길이, P= 부분 문자열 길이
# st = 문자열
# check = 문자열 최소 개수 (A,C,G,T 순서)
import sys

sys_input = sys.stdin.readline 
S, P = map(int,sys_input().split())

st = sys_input().rstrip('\n')
check = list(map(int,sys_input().split()))

dic = {k:0 for k in ['A','C','G','T']}
result = 0
for i, s in enumerate(st):
    if i < P:
        dic[s] += 1
    else:
        prev_s = st[i-P]
        dic[prev_s] -= 1
        dic[s] += 1

    if i+1 >= P:
        for j,k in enumerate(dic): 
            if dic[k] < check[j]:
                break
        else:
            result += 1
print(result)


