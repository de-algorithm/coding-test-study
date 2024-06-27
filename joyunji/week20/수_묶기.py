n = int(input())
series = [int(input()) for _ in range(n)]

def solution(n, series):
	positive = [e for e in series if e > 1]
	positive.sort(reverse=True)
	negative = [e for e in series if e <= 0]
	negative.sort()
	cnt_one = series.count(1)
	answer = cnt_one 
	for i in range(0, len(positive)-1, 2):
		answer += positive[i] * positive[i+1]
	if len(positive)%2 == 1:
		answer += positive[-1]

	for i in range(0, len(negative)-1, 2):
		answer += negative[i]*negative[i+1]
	if len(negative)%2 == 1:
		answer += negative[-1]
		
	return answer
print(solution(n, series))