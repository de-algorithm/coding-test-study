n = int(input())

# input list of period
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

period = []

# list of period 값 치환
for _ in range(n):
	start_m, start_d, end_m, end_d = map(int, input().split())
	start = sum(month[:start_m]) + start_d
	end = sum(month[:end_m]) + end_d
	period.append([start, end])
period.sort()


def solution(n, period):
	global min_flower
	min_flower = n+1
	visited = [0 for _ in range(n)]
	for i, (ps, pe) in enumerate(period):
		if ps <= 60:
			visited[i] = 1
			dfs(period, visited, pe, 1)
			visited[i] = 0
	if min_flower > n:
		return 0
	return min_flower

def dfs(period, visited, e, cnt):
	global min_flower
	if (e > 334):
		min_flower = min(min_flower , cnt)
		return
	
	for p in range(len(period)):
		ps, pe = period[p]
		if ps < e and visited[p] == 0:
			visited[p] = 1
			dfs(period, visited, max(e, pe), cnt + 1)
			print(cnt)
			visited[p] = 0
  

print(solution(n, period))