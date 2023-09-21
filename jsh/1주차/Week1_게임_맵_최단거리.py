# Lv. 2
# BFS로 풀 생각
# 시작시간 : 12:50
# 끝난시간 : 13:15
# BFS로 풀 생각
"""
1. 첫시작은 1,1

2. def bfd (x,y) 를 사용해서 현재기준 [ 상 하 좌 우 ]를 하나씩 체크해    있을경우 count += 1 하고 해당 위치로 이동하기
2-1. deque에는 (x, y, visited) 세개의 값이 들어간다 ( 가로, 세로, 방문횟수 )

"""
from collections import deque
def bfs(maps):
    max_x, max_y = len(maps), len(maps[0])
    result_deque = deque()
    result_deque.append((0,0,1))
    # x, y, 방문횟수
    
    move_x = [ 1, -1, 0, 0 ]
    move_y = [ 0, 0, 1, -1 ]
    # 오른쪽, 왼쪽, 위, 아래로 한칸씩움직이기 위해 선언
    
    
    while result_deque:
        x, y, count = result_deque.popleft()
        maps[x][y] = 0
        for i in range(4):
            current_x =  x + move_x[i]
            current_y =  y + move_y[i]
            if current_x == max_x-1 and current_y == max_y-1:
                count += 1
                return count
            if -1 < current_x < max_x and -1 < current_y < max_y and maps[current_x][current_y] :
                # print(current_x,current_y, maps[current_x][current_y])
                result_deque.append((current_x, current_y, count + 1))
                maps[current_x][current_y] = 0
    
    return -1
    
def solution(maps):
    # print(maps[3][2])
    return bfs(maps)
    # return 0
    
    

# 정확성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.06ms, 10.4MB)
# 테스트 4 〉	통과 (0.03ms, 10.2MB)
# 테스트 5 〉	통과 (0.03ms, 10.4MB)
# 테스트 6 〉	통과 (0.06ms, 10.3MB)
# 테스트 7 〉	통과 (0.06ms, 10.3MB)
# 테스트 8 〉	통과 (0.04ms, 10.3MB)
# 테스트 9 〉	통과 (0.08ms, 10.4MB)
# 테스트 10 〉	통과 (0.05ms, 10.2MB)
# 테스트 11 〉	통과 (0.03ms, 10.2MB)
# 테스트 12 〉	통과 (0.02ms, 10.4MB)
# 테스트 13 〉	통과 (0.03ms, 10.3MB)
# 테스트 14 〉	통과 (0.03ms, 10.2MB)
# 테스트 15 〉	통과 (0.03ms, 10.3MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)
# 테스트 17 〉	통과 (0.04ms, 10.2MB)
# 테스트 18 〉	통과 (0.01ms, 10.2MB)
# 테스트 19 〉	통과 (0.01ms, 10.1MB)
# 테스트 20 〉	통과 (0.01ms, 10.2MB)
# 테스트 21 〉	통과 (0.01ms, 10.2MB)
# 효율성  테스트
# 테스트 1 〉	통과 (23.56ms, 10.3MB)
# 테스트 2 〉	통과 (3.41ms, 10.2MB)
# 테스트 3 〉	통과 (8.51ms, 10.2MB)
# 테스트 4 〉	통과 (5.02ms, 10.3MB)