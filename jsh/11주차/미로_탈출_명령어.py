# 출발지에서 탈출지까지의 거리를 먼저 구해놓는다 최소 이동횟수 ( end_cnt )
# https://limsb-dev.tistory.com/6 
# 비슷하게 접근하려한듯

def solution(n, m, x, y, r, c, k):
    answer = ''
    
    end_cnt = abs(r - x) + abs ( c - y)
    
    
    # 탈출 지점에 도착 후, 두 번 이동하면 제자리로 돌아올 수 있습니다. 따라서 (k - dist)가 짝수가 되어야 합니다.
    if k < end_cnt or (k - end_cnt) % 2 ==  1 :
        return 'impossible'
    
    
    # 출발지와 도착지를 알고 있으니깐 얼마나 이동해야하는지 계산할 수 있지 않을까? 
    cnt_dict = { 'd' : 0, 'l' : 0, 'r':0, 'u':0}
    
    if x > r :
        cnt_dict['u'] += x - r
    else :
        cnt_dict['d'] += r - x
        
        
    if y > c :
        cnt_dict['l'] += y - c
    else :
        cnt_dict['r'] += c - y
    
    answer += 'd' * cnt_dict['d']
    
    return answer