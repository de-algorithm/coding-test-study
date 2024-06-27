# def solution(N, pos):
#     """선 긋기
#     https://www.acmicpc.net/problem/2170

#     Args:
#         N (int): 선을 그은 횟수
#         pos (list[tuple[int]]): 선을 그을 때 선택한 두 점의 위치
        
#     Returns:
#         int : 그은 선의 총 길이 
#     """
#     pos.sort()
#     sum = pos[0][1]-pos[0][0]
#     for i in range(1, N):
#         if pos[i-1][1] >= pos[i][0]:
#             sum += pos[i][1]-pos[i-1][1]
#         else:
#             sum += pos[i][1]-pos[i][0]
    
    
#     return sum

# # N = 4
# # pos = [[1,3],[2,5],[3,5],[6,7]]


# N = int(input())
# pos = []
# for _ in range(N):
#     pos.append(tuple(map(int, input().split())))
    
# print(solution(N, pos))

import sys

n = int(input())
coords = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

def solution(n, coords):
	coords.sort()
	start, end = coords[0]
	answer = 0
	
	
	for i in range(1, n):
		# 겹칠 떄 
		if coords[i][0] <= end < coords[i][1]:
			end = coords[i][1]
		# 안겹칠 때
		elif end < coords[i][0]:
			answer += (end - start)
			start = coords[i][0]
			end = coords[i][1]
		
	
	return answer + (end - start)

print(solution(n, coords))