import sys
input = sys.stdin.readline
N, C = map(int, input().split())
M = int(input())

box_list = []

for _ in range(M):
	box_list.append(list(map(int, input().split())))

box_list.sort(key = lambda x : (x[1], x[0]))
print(box_list)
# n +1 을 하는 이유는 마을의 개수와 index 번호를 맞추기 위해
count_truck = [ 0 for _ in range( N + 1 ) ]
total = 0
cap = 0
pre_start, pre_end = 0, 0 
for i in range(len(box_list)):
	start, end, amount = box_list[i]
	if pre_start < start:
		# 상자 내리기
		total += count_truck[start]
		cap -=count_truck[pre_start]
	if pre_start<= start:
		# 여유 공간이 있다면 상자 싣기
		if cap < C:
            # 현재 용량+amount가 최대용량과 같거나 작을 때 
			if cap+amount <= C:
				cap += amount
				count_truck[end] += amount
            # 초과할 때 
			else:
				cap = C
				count_truck[end] += (C-cap)
	
	pre_start = start
	print(end)
	print(count_truck)
	print(total)
  
print(sum(count_truck))