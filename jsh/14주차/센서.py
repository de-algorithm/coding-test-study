# 첫째 줄에 센서의 개수 N(1 ≤ N ≤ 10,000), 둘째 줄에 집중국의 개수 K(1 ≤ K ≤ 1000)가 주어진다. 셋째 줄에는 N개의 센서의 좌표가 한 개의 정수로 N개 주어진다. 각 좌표 사이에는 빈 칸이 하나 있으며, 좌표의 절댓값은 1,000,000 이하이다.

"""
예제 입력 1 
6
2
1 6 9 3 6 7
예제 출력 1 
5


[1 3 6 6 7 9]

{ 2 3 0 1 2}
-> ( 1 3 ), ( 6 6 7 9 )
--> 2 + 1+ 2 => 5
"""

"""
예제 입력 2 
10
5
20 3 14 6 7 8 18 10 12 15
예제 출력 2 
7


[ 3 6 7 8 10 12 14 15 18 20 ]
{  3 1 1 2  2  2  1  3  2}
---> 
( 3 ), ( 6 7 8 10 ),( 12 ), ( 14 15 ), ( 18 20)
=>      1 + 1 + 2 +             1 +        2
==>   7

"""


def solution():
    import sys
    input = sys.stdin.readline

    N = int(input())  
    K = int(input())  
    sort_list = sorted(list(map(int,input().split())))
    answer = 0
    
    diff_pos = []
    
    for i in range(1, N ):
        diff_pos.append(sort_list[i]-sort_list[i-1])
    
    sort_diff_pos = sorted(diff_pos, reverse = True)[K-1 : ]
    
    
    
    print(sum(sort_diff_pos))



if __name__ == '__main__':
    solution()