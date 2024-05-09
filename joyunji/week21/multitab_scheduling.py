import sys
from collections import Counter
input = sys.stdin.readline


N, K = map(int, input().split())
devices = list(map(int, input().split()))
count = Counter(devices) 
multitab = []
answer = 0
min_count = 101
for i in range(K):
	if devices[i] in multitab:
		continue
	else:
		# 멀티탭에 빈자리가 있다면 꼽기
		if len(multitab) < N:
			multitab.append(devices[i])
	    # 빈자리가 없다면 
		else:	
			change = 0  # 사용횟수 최소인 기기 번호 
			for m in multitab:
				if count[m] < min_count:
					min_count, change = count[m], m
			print("change", change)
			# 사용횟수가 최소로 남은 기기를 빼고
			multitab.remove(change)
			# 현재 기기 꼽는다. (사용횟수 -1, 뽑기 +1) 
			count[devices[i]] -=1
			multitab.append(change)
			answer += 1
			print(answer)

print(answer)