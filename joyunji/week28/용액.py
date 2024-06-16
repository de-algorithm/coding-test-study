import sys
input = sys.stdin.readline
N = int(input())
liquids = list(map(int, input().split()))

left, right = 0, N-1
min_value = 2000000000
answer1, answer2 = 0, 0

while left < right:

    value = liquids[left] + liquids[right]
    
    if abs(value) <= min_value:
        answer1, answer2 = liquids[left], liquids[right]
        min_value = abs(value)
    
    if value <= 0:
        left += 1
    else:
        right -= 1


print(answer1, answer2)