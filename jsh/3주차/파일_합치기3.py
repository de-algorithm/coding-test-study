# start > 13:40
# 1차 끝 > 14:00 하지만 시간초과...

# 2차 시작 > 14:00
# end > 14:05
# 근데 이건 heqp 라이브러리 보면서 했음



# Gold 4

# 뭐이리 한글이 어렵지 이건



# 정렬하는데 시간이 오래걸리는 것 같다 heap을 써보자
import heapq
test_cnt = int(input())
for _ in range(test_cnt):
    n = int(input())
    val = list(map(int, input().split()))
    heapq.heapify(val)
    sum = 0
    while len(val) > 1 :
        a = heapq.heappop(val)
        b = heapq.heappop(val)
        sum += a+b
        heapq.heappush(val, a+b)
    print(sum)

"""아래 방식으로 하니깐 시간초과"""
# test_cnt = int(input())
# for _ in range(test_cnt):
#     n = int(input())
#     val = list(map(int, input().split()))
#     sum = 0
#     while len(val) > 1 :
#         val.sort(reverse = True)
#         a = val.pop()
#         b = val.pop()
#         sum += a+b
#         val.append(a+b)
#         # print(sum,val)
#     print(sum)
    
    
    