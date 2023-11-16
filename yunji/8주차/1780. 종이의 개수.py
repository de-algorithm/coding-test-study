import sys
sys.stdin = open('yunji/input.txt', 'r')

# NxN 행렬 입력 받기
N = int(sys.stdin.readline()) # 1 ≤ N ≤ 37, N은 3^k 꼴
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

# 1. 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
# 2. (1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.

answer = [0, 0, 0] # -1, 0 ,1 순서 종이 개수 

def check(arr, N):
    # 1. 종이가 모두 같은 수로 되어 있다면
    # 해당 수의 종이 개수 계산 
    first_element = arr[0][0]
    if isEqual(arr, first_element):
        answer[first_element+1] += 1

    # 2. (1)이 아니라면 종이를 9등분으로 자르고
    # 9등분에 대해 check() 호출
    else:
        tmp = N//3
        for i in range(0, N, tmp):
            for j in range(0, N, tmp):
                arr1 = [row[j:j+tmp] for row in arr[i:i+tmp]]
                # print(arr1)
                check(arr1, tmp)
def isEqual(arr1, first_element):
    # 모든 요소를 비교하여 같은지 확인
    for row in arr1:
        for element in row:
            if element != first_element:
                return False

    # 모든 요소가 같으면 True 반환
    return True
    
check(arr, N)

for i in answer:
    print(i)
    
'''
import sys
sys.stdin = open('yunji/input.txt', 'r')
input = sys.stdin.readline

N = int(input())
array = [list(map(int, input().strip().split(' '))) for _ in range(N)]


answer = [0, 0, 0]

def dfs(N, x, y):
    tmp = array[x][y]
    
    if N == 1:
        answer[tmp+1] += 1
        return

    for i in range(x, x+N):
        for j in range(y, y+N):
            if array[i][j] != array[x][y]:
                for a in range(x, x+N, N//3):
                    for b in range(y, y+N, N//3):
                        dfs(N//3, a, b)

                return
    
    answer[tmp+1] += 1

dfs(N, 0, 0)

print('\n'.join(map(str, answer)))
'''