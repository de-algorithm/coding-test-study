# 시작 : 15 : 40
# 끝 :  16:40

"""
3
3 4 5
1 0 1 0

[]
[ 3+4, 3*4 ]
[ 3+4*5, 3*4+5] => [35, 17]

"""
"""
6
1 2 3 4 5 6
2 1 1 1

[ 1+2, 1+2, 1-2, 1*2, 1/2]
[ 1+2+3, ]


계산식을 하나의 배열로 바꾸자
2 1 1 1 
-> [ + + - * / ]

수식을 순열로 만들자
> permutations 활용

하나의 수식 순열에 대해 고정된 값 배열을 넣어 결과값을 all_result에 넣은 뒤 min max를 통해 가져온다

"""
from itertools import permutations
import sys
n = int(input())
data = list(map(int, input().split()))
arr = list(map(int , input().split()))

calculator = ['+','-','*','/']
cal_arr = []
for i in range(4):
    for j in range(arr[i]):
        cal_arr.append(calculator[i])

        
permutation_list = set(permutations(cal_arr, len(cal_arr)))

all_result = []
for permu in permutation_list:
    result = data[0]
    for i in range(len(permu)):
        if permu[i] == '+' :
            result += data[i+1]
        elif permu[i] == '-' :
            result -= data[i+1]
        elif permu[i] == '*' :
            result *= data[i+1]
        elif permu[i] == '/' :
            if result * data[i+1] < 0 :
                result = -1 *(abs(result)//abs(data[i+1]))
            else:
                result = (result // data[i+1])

    all_result.append(result)
    
    
print(max(all_result))
print(min(all_result))