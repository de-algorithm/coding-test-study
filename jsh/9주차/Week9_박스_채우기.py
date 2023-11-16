## 분할 + 그리디가 필요하다 생각
## -> 그리디만으로 풀 수 있찌 않을까?
## -> 부피가 큰 큐브부터 채워보자






import sys
input = sys.stdin.readline

from collections import defaultdict, deque


def solution():
    x, y, z = 4, 4, 8
    # x,y,z =  map(int,input().split())
    # check_arr = [[0,0,0] for _ in range(x*y*z) ]
    # print(check_arr)
    n = 3
    # n = int(input())
    cube = defaultdict(int)
    cube[0] = 10
    cube[1] = 10
    cube[2] = 1
    print(cube)
    cube = sorted(cube, reverse = True)
    
    # for _ in range(n):
    #     len,val =  map(int,input().split())
    #     cube[len] = val
        
    print(cube)
    
    




if __name__ == '__main__':
    solution()