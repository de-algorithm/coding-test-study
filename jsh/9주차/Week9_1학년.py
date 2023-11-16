# 완전탐색돌려서 0~20 사이가 나오게하면 되는거 아닌가?

from collections import deque
import sys
input = sys.stdin.readline

"""
ex ) 11 / 8 3 2 4 8 7 2 4 0 8 8
[ 0 ~ 20 ] 까지 있는 배열을 n 개 생성 ( = 2차원 배열 )
1번 째 : 8 에 1, 나머진 0
2번 째 ( 8-3, 8+3 ) : 5와 11에 1, 나머진 0
3번 째 ( 5 -2, 5+2, 11-2, 11+2) 에 1, 나머지 0
.,..
중복된 것이 있으면 2, 3, 4 ... += 1

사진 참고
-> https://codedrive.tistory.com/451


"""

def solution():
    n = int(input())
    nums = list(map(int, input().split()))
    
    result_list = [[0 for _ in range(21) ] for _ in range(n)]
    
    result_list[0][nums[0]] = 1
    
    for i in range(1, n-1):
        for j in range(21):
            if j+nums[i] <= 20:
                result_list[i][j+nums[i]] += result_list[i-1][j]
            if 0<= j-nums[i] :
                result_list[i][j-nums[i]] += result_list[i-1][j]
                

    print(result_list[n-2][nums[-1]])
    
    
    
    


if __name__ == '__main__':
    solution()
    
    
    
    

# # 메모리 초과 
# def solution():
#     n = int(input())
#     nums = list(map(int, input().split()))
#     nums = deque(nums)
#     result = nums.pop()
    
#     sequence = deque()
#     sequence.append(nums.popleft())

#     for i in range(1, n-1) :
#         append_num = nums.popleft()
#         len_seq = len(sequence)
#         for j in range(len_seq):
#             seq = sequence.popleft()
#             if seq+append_num <= 20 :
#                 sequence.append(seq+append_num)
#             if seq-append_num >= 0 :
#                 sequence.append(seq-append_num)
#     print(sequence.count(result))
    