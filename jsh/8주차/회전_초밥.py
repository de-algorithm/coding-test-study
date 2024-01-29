# [ BOJ ] / Gold 4 / 

# 메모리 : 166508 KB
# 시간 : 4630ms

# 처음엔 list 에 set을 사용해서 unique 값을 count 하는 것을 생각
# -> 그렇게 생각하다보니 dict가 생각나서 dna 문제에 사용했엇던 이론을 쓰는게 더 간편하지 않을까 생각
# 


# 입력시간초과??
import sys
input = sys.stdin.readline


from collections import defaultdict
def solution():
# 회전 초밥 벨트에 놓인 접시의 수 N, 초밥의 가짓수 d, 
# 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
    N, d, k, c  = map(int,input().split())
    shusi_list = []
    for _ in range(N):
        shusi_list.append(int(input()))

    # https://ryu-e.tistory.com/33
    # arr.extend(arr)   # 원형이라서 2개를 이어준다.
    shusi_list.extend(shusi_list)
    
    
    shusi_dict = defaultdict(int)
    start, end = 0, k-1
    max_cnt = 0
    
    shusi_dict[c] = 1
    
    check_arr = shusi_list[start : end]
    for word in check_arr :
        shusi_dict[word] += 1
    
    while end  < len(shusi_list):
        shusi_dict[shusi_list[end]] += 1
        
        max_cnt = max(max_cnt, len(shusi_dict))
        shusi_dict[shusi_list[start]] -= 1
        
        # 개수가 0이어도 len을 쓰면 count가 되기 때문에 제거하는 코드 추가
        if shusi_dict[shusi_list[start]] == 0 :
            del shusi_dict[shusi_list[start]]
        
        start += 1
        end += 1
        
    print(max_cnt)
    
    



if __name__ == '__main__':
    solution()
    