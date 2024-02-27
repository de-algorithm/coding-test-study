# start ->  13:20
# end   ->  14:00

"""
종이의 첫번째 [ 0, 0 ]값을 기준으로(check_block) 다음 블럭과 비교하여 같은지 아닌지 비교
-> 같으면 넘어가고
-> 다르면 종이를 또 3분할 하여 위 단계 다시 진행

"""

import sys
input = sys.stdin.readline


def check(start_x, start_y, len):
    global arr, block
    check_block = arr[start_x][start_y]
    
    for cur_x in range(start_x, start_x + len):
        for cur_y in range(start_y, start_y + len):
            if check_block != arr[cur_x][cur_y]:
                new_len = len//3
                
                for new_x in range(0,3):
                    for new_y in range(0,3):
                        check(start_x + new_len * new_x, start_y + new_len * new_y, new_len)
                return 0
    
    block[check_block] += 1
                
    



def solution():
    # N = 9
    # arr = [[0, 0, 0, 1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 1, -1, -1, -1], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 1, -1, 0, 1, -1, 0, 1, -1], [0, -1, 1, 0, 1, -1, 0, 1, -1], [0, 1, -1, 1, 0, -1, 0, 1, -1]]
    global arr,block
    
    N = int(input())
    block = {-1 : 0, 0 : 0, 1 : 0  }
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
        
    check(0,0, N)
    
    print(block[-1])
    print(block[0])
    print(block[1])

if __name__ == '__main__':
    solution()