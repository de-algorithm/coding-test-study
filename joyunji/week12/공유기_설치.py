import sys
sys.stdin = open('yunji/input.txt', 'r')
input = sys.stdin.readline

# N: 집의 개수, C: 공유기의 개수
N, C = map(int, input().split())
x = [int(input()) for _ in range(N)]

x.sort()            # 정렬
left = 1
right = x[-1] - x[0] # 가장 멀게 공유기를 설치했을 때 최대 거리


while left <= right:
    mid = (left + right) // 2   # 현재 공유기 간의 거리
    install = x[0]              # 첫번째 집에 우선 설치
    count = 1
    
    # 공유기 설치를 몇 대까지 할 수 있는지 확인
    for i in range(1, len(x)):
        if x[i] >= install + mid:   # 앞에 공유기 설치된 집과 현재 집 간의 거리가 mid와 같거나 클 때
            count += 1              # 공유기 설치 
            install = x[i]          # 다음 집과 거리를 비교할 공유기 설치된 집으로 갱신 
    
    # 공유기 설치 수가 C개보다 같거나 크면 공유기 사이 거리를 늘림
    if count >= C:
        left = mid + 1
        answer = mid
    # 공유기 설치 수가 C보다 작으면 공유기 사이 거리 줄임
    else:
        right = mid - 1
        
print(answer)
    