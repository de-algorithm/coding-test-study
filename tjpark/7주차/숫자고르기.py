# 10:30

# 첫 째줄은 1~N까지 차례대로로 있다.
# 첫 째줄에서 뽑은 숫자의 집합과
# 첫 째줄에서 바로 밑에 있는 정수들의 집합이 같아야함
# 이러한 조건을 만족시키도록 정수들을 최대로 많이 뽑는 방법을 찾아라

# input
# N= 첫째 줄 정수 개수 1~N
# 둘째 줄에 들어가는 정수 순서대로 하나씩 입력됨

#return
# 첫째 줄: 뽑힌 정수들의 개수
# 작은 수 부터 큰수 순서로 하나씩 출력

# 최대개수를 구하려면 완전탐색이 맞는듯
# 시간 제한 1초 생각해야함
# 중복된 숫자는 뽑히면 안됨
# 집합에 없는 숫자를 뽑으면 안됨
import sys

sys_input = sys.stdin.readline

N = int(sys_input())
# dfs를 활용해 cycle이 생기는곳은 모두 count
line = [int(sys_input()) for _ in range(N)]

def dfs(num):
    global result
    # 방문했는지 check
    if visited[num] == 0:
        visited[num] = 1
        
        # 윗줄과 연결된 아랫줄 집합 추가
        line1.add(num+1)
        line2.add(line[num])

        # 집합이 같다면 결과에 포함시킴
        if line1 == line2:
            result = result | line2
            return
        dfs(line[num]-1)
    visited[num] = 0

# 결과 저장용
result = set()

for i in range(N):
    visited = [0] * N
    line1 = set()
    line2 = set()
    dfs(i)

result = list(set(result))
result.sort()
print(len(result))
for i in result:
    print(i)



'''
# 4%에서 실패 (set만들 때 자동 정렬되는 줄 알았으나 안됨)
# set으로 중복하지 않은 값을 활용해 후보군을 제거해 나가는 방식

line1 = [i+1 for i in range(N)]
line2 = [int(sys.stdin.readline()) for i in range(N)]
line1_set = set(line1)

while(1):    
    line2_set = set(line2)
    cal_set = line1_set-line2_set
    # 두 집합이 같으면 멈춤 
    if not cal_set:
        break
    else:
        line1_set.add(0)
        for i in cal_set:
            # line1_set의 i를 찾아 제거
            line1_set.remove(i)
            # line2 리스트의 i-1번째 0으로 변경
            line2[i-1] = 0

line2_set.discard(0)
result = list(line2_set)
result.sort()
print(len(result))
for i in result:
    print(i)


# 1.두번 째 줄을 중복제거 후 첫 번째 줄과 비교
# 2.두번 째 줄에 없은 것이 있으면 해당 번호에 해당하는 첫번 째줄과 두번째 줄 삭제
# 1번으로 돌아가 반복


1 2 3 4 5 6 7
3 2 1 6 7 8 1

차집합
1 2 3 6 7
3 2 1 8 1

차집합
1 2 3 
3 2 1
'''