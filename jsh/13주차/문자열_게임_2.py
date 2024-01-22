# 문제
# 작년에 이어 새로운 문자열 게임이 있다. 게임의 진행 방식은 아래와 같다.

# 알파벳 소문자로 이루어진 문자열 W가 주어진다.
# 양의 정수 K가 주어진다.
# 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
# 어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.
# 위와 같은 방식으로 게임을 T회 진행한다.

# 입력
# 문자열 게임의 수 T가 주어진다. (1 ≤ T ≤ 100)

# 다음 줄부터 2개의 줄 동안 문자열 W와 정수 K가 주어진다. (1 ≤ K ≤ |W| ≤ 10,000) 



# 예제 입력 1 
# 2
# superaquatornado
# 2
# abcdefghijklmnopqrstuvwxyz
# 5
# 예제 출력 1 
# 4 8
# -1
# 첫 번째 문자열에서 3번에서 구한 문자열은 aqua, 4번에서 구한 문자열은 raquator이다.

# 두 번째 문자열에서는 어떤 문자가 5개 포함된 문자열을 찾을 수 없으므로 -1을 출력한다.

# 예제 입력 2 
# 1
# abaaaba
# 3
# 예제 출력 2 
# 3 4


"""
첫번 째 접근 
w.count(문자)
로 해서 k 의 개수보다 큰 단어로 index를 찾아 해보자

=> 개선

그럴거면 어짜피 문자열 index를 dict에 하나씩 배열로 추가해서 개수 비교 해서 k보다 많이 있을 때 index의 개수를 비교해서 min max를 구할 수 있지 않을까?

"""

import sys

def sol(w, k):
    dict = {}
    min_val = 10001
    max_val = -1
    
    for idx in range(len(w)):
        if w[idx] in dict :
            dict[w[idx]].append(idx)
        else :
            dict[w[idx]] = [idx]
    
    for key,array in dict.items():
        start = 0
        end = start + k - 1
        if len(array) < k:
            continue
        while end < len(array):
            length = array[end] - array[start] + 1
            min_val = min(min_val, length)
            max_val = max(max_val, length)
            start += 1 
            end += 1
        
    # print(dict)
            
    
    return min_val,max_val 

def solution():
    t = int(input())
    for i in range(t):
        w = sys.stdin.readline().rstrip()
        k = int(input())
        
        min_val,max_val = sol(w,k)
        if min_val == -1 or max_val == -1:
            print(-1)
        else :
            print(min_val,max_val)
        
        
    
    

def test():
    t = 2
    w_1 = 'superaquatornado'
    k_1 = 2
    min_val,max_val = sol(w_1,k_1)
    if min_val == -1 or max_val == -1:
        print(-1)
    else :
        print(min_val,max_val)
    
    
    w_2 = 'abcdefghijklmnopqrstuvwxyz'
    k_2 = 5
    min_val,max_val = sol(w_2,k_2)
    if min_val == -1 or max_val == -1:
        print(-1)
    else :
        print(min_val,max_val)


if __name__ == '__main__':
    # test()
    solution()
    