'''
problem: https://www.acmicpc.net/problem/7570
'''

# import sys
# input = sys.stdin.readline
# N = int(input())
# line = list(map(int, input().split()))

def solution(N, line):
	answer = 0
	idx = [0 for _ in range(N+1)] # N번호와 인덱스를 맞추기 위해 
	i = 1
	for n in line:
		idx[n] = i
		i += 1
	
	count = 0 # 연속적으로 증가하는 수열의 최대 개수
	temp = idx[1]
	for i_ in idx[2:]:
		if temp < i_:
			count += 1
		else:
			answer = max(answer, count)
			count = 0
		temp = i_
	answer = max(answer, count)
	return N-(answer+1)
N = 5
line = [1,2,3,4,5]
print(solution(N, line))
    
    


