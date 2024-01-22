import sys
input = sys.stdin.readline

"""
결국 가장 큰 차이가 안나게 중복된 색상의 보석을 분배해야한다는거

예제 2
7 5
[7 1 7 4 4]
라 한다면

7명에게 5종류의 보석을 준다햇을 때

답이 4가 나왔는데

7명에게
[aaaa, aaa, b, cccc, ccc, dddd, eeee] 로 주면 되는거

그러면 입력받은 배열을 정렬한 후, 최소 최대의 중간값을 찾아서 각 색상의 개수를 중간값으로 나누어가면서 개수를 세어보자.
까지가 나의 의견. 구현 못해서 다른 사람이 한 거 보고 작성
https://velog.io/@deankang97/%EB%B0%B1%EC%A4%80-2792-%EB%B3%B4%EC%84%9D%EC%83%81%EC%9E%90
"""

def solution():
    
    N,M = map(int, input().split())
    colors = []
    
    for _ in range(M):
        colors.append(int(input()))
    
    colors.sort()
    
    print(f'colors = {colors}')
    left = 1
    right = colors[-1]
    
    res = 0
    
    while left <= right :
        mid = (left + right) // 2
        sum =0
        print(f' left : {left}, right : {right}, mid : {mid}')
        for color in colors :
            if color % mid == 0 :
                print(f'color : {color}, mid : {mid}, color % mid = 0 ')
                cnt = color // mid
            else :
                print(f'color : {color}, mid : {mid}, color % mid != 0 ')
                cnt = color // mid + 1
            sum += cnt
            print(f'cnt = {cnt}, sum = {sum}')
        if sum > N :
            print(f' 전체 나눠준 인원이 N 보다 크기 때문에 left = mid + 1')
            left = mid + 1
        else :
            print(f' 전체 나눠준 인원이 N 보다 작기 때문에 right = mid  -1')
            res = mid
            right = mid - 1
        
        print(f'left = {left}, right = {right}')
    
    print(res)
if __name__ == '__main__':
    solution()
    