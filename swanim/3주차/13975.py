'''
힙 사용
비용 저장 변수 생성
'''
import heapq

for _ in range(int(input())):
    k = int(input())
    hq = []
    ls = list(map(int, input().split()))
    
    for i in ls:
        heapq.heappush(hq, i)
    
    ans = 0
    while True:
        if len(hq) <= 1:
            break
        else:
            a = heapq.heappop(hq)
            b = heapq.heappop(hq)

            ans += a + b
            heapq.heappush(hq, a+b)
    
    print(ans)