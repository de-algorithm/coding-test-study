import sys
from collections import defaultdict
sys.stdin = open('yunji/input.txt', 'r')

def check(dic, DNA_use):
    if dic['A'] >= DNA_use[0] and dic['C'] >= DNA_use[1] and dic['G'] >= DNA_use[2] and dic['T'] >= DNA_use[3]:
        return True
    return False
S, P = map(int, sys.stdin.readline().split())
DNA_str = sys.stdin.readline()
DNA_use = list(map(int, sys.stdin.readline().split())) # A C G T 
dic = {'A': 0, 'C': 0 , 'G': 0, 'T': 0}


cnt = 0
curr_sub = DNA_str[:P]

# 처음 부분문자열 개수 계산하기
for c in curr_sub:
    dic[c] += 1

if check(dic, DNA_use):
    cnt += 1
    
for i in range(1, S-P+1):
    dic[curr_sub[0]] -= 1
    curr_sub = DNA_str[i:i+P]
    dic[curr_sub[-1]] += 1
    if check(dic, DNA_use):
        cnt += 1

print(cnt)

