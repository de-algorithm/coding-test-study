# 두개의 파일을 합침
# 파일을 합칠 때의 비용은 두 파일의 크기 합
# 최종 파일 완성에 필요한 비용 구하기

# 최소값 끼리만 더해가면 최비용을 구할 수 있음
import sys
import heapq

T = int(sys.stdin.readline())

page_list = []
for i in range(T*2):
    if i % 2 == 0:
        sys.stdin.readline()
    else:
        page = (list(map(int,sys.stdin.readline().split())))
        heapq.heapify(page)
        page_list.append(page)

for page in page_list:
    result = 0 
    while len(page) > 1:
        min_val = heapq.heappop(page)
        min_val += heapq.heappop(page)
        result += min_val
        heapq.heappush(page, min_val)

    print(result)





