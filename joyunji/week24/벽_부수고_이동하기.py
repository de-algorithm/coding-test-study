import sys
input = sys.stdin.readline

T = int(input())

def dfs(i):
    global team_stu
    visited[i] = True
    team.append(i) # 팀에 i번 학생 추가
    n = num[i] #  i번 학생이 선택한 학생 
    
    if visited[n]: # 선택된 학생을 방문한 적 있다면
        if n in team: # 팀에 포함되어 있다면 
            team_stu += len(team[team.index(n):]) # 이 학생부터 이후에  
            # print(team[team.index(n):])
            return 
    else:
        dfs(n)
        
for _ in range(T):
	N = int(input())
	# 학생 번화와 인덱스 맞추기 위해 0번 인덱스 생성  
	num = [0] + list(map(int, input().split()))
	
	visited = [False] * (N+1)
	team_stu = 0 # 팀이 된 학생 수
	
	for i in range(1, N+1):
		if not visited[i]:
			team=[]
			dfs(i)
	print(N-team_stu)