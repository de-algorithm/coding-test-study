# 완전탐색을 생각
# 근데 이미 갔엇던 지점을 또 가면 먼저 갔었던 것이 무조건 이득이니깐 visited를 만드는게 이득이라 생각

# 텔레포트는 해도 시간이 0 이 소모되니깐 1순위로 텔레포트
# 2,3 순위는 +-로 생각하여 진행


from collections import deque
import sys

input = sys.stdin.readline


def solution():
    N,K = map(int, input().split()) 
    # 0 ~ 100,000 까지 배열 선언
    dist = [0]*100001
    
    deq = deque()
    deq.append(N)
    
    while deq:
        pos = deq.popleft()
        # print(f'pos = {pos}')
        if pos == K :
            print(dist[pos])
            break
        
        for next in (pos*2, pos-1, pos+1):
            if  0 <= next <= 100000 and dist[next] == 0 :
                if next == pos*2 :
                    dist[next] = dist[pos]
                else :
                    dist[next] = dist[pos] +1
                
                
                deq.append(next)

                
    

if __name__ == '__main__':
    solution()