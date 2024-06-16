import sys
from collections import defaultdict
input = sys.stdin.readline
M, N = map(int, input().split())
dic = defaultdict(int)


for _ in range(M):
    size = list(map(int, input().split())) 
    # 구성 같은 행성은 한개만 세기 
    rank_dict = {value: rank for rank, value in enumerate(sorted(set(size)))}
    ranks = tuple(rank_dict[s] for s in size)
    dic[ranks] += 1
	
answer = 0

for v in dic.values():
    answer += (v*(v-1))//2
        
print(answer)