import sys
sys.stdin = open('yunji/input.txt', 'r')

input = sys.stdin

L, W, H = map(int, input.readline().split())    # 박스 l, w, h 
V = L*W*H
N = int(input.readline())                       # 큐브 종류 개수
arr = [tuple(map(int, input.readline().split())) for _ in range(N)]                                     # 큐브 종류 : 큐브 개수
arr.sort(reverse=True)
    
answer, tot_cnt = 0, 0 
for idx, cnt in arr:
    tot_cnt *= 8 # 현재 큐브로 채울 수 있는 개수 (4x4x4 1개 = 2x2x2 8개)
    len = 2**idx    # 큐브 한 변 길이
    
    cnt_limit = (L//len)*(W//len)*(H//len) - tot_cnt # 채울 수 있는 최대한 개수 - 지금까지 (현재 큐브 기준으로)채운 개수 = 채울 수 있는 최대 큐브 개수
    cnt_limit = min(cnt, cnt_limit) # 실제로 채우기 가능한 개수 = 채울 수 있는 최대 큐브 개수와 현재 큐브 개수 중 작은 개수
    
    answer += cnt_limit # 채울 수 있는 큐브 개수 추가 
    tot_cnt += cnt_limit # 

# tot_cnt는 최종적으로 1x1x1 큐브로 상자를 채울 수 있는 개수이며 상자 부피와 동일
if tot_cnt == V:
    print(answer)
else: # 박스를 채울 수 없다면 -1
    print(-1)
    


