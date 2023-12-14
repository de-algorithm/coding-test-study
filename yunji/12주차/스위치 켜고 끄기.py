'''
남학생 (1) : 스위치 번호가 받은 수의 배수 -> 스위치 상태 변경
여학생 (2) : 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 
        그 구간에 속한 스위치의 상태를 모두 바꾼다. 
        이때 구간에 속한 스위치 개수는 항상 홀수가 된다.
        
        대칭되는 구간이 없다면 받은 번호의 스위치만 상태 변경
'''
import sys
sys.stdin = open('yunji/input.txt', 'r')
input = sys.stdin.readline


switch = int(input()) # 스위치 개수
state = [0] + list(map(int, input().split()))    # 스위치 상태 리스트
student = int(input())  # 학생 수
# print(state[1:])

for _ in range(student):
    gender, num = map(int, input().split())
    # 남학생
    if gender == 1:
        for i in range(1, switch+1):
            if i % num == 0:
                state[i] = 1-state[i]
    # 여학생
    else:
        # 좌우 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서 상태를 모두 바꾼다.
        # 받은 번호 스위치부터 상태변경
        state[num] = 1-state[num]
        for i in range(1, min(switch-num, num-1)+1):
            if state[num-i] == state[num+i]:
                state[num-i] = 1-state[num-i]
                state[num+i] = 1-state[num+i]
            else:
                break
    # print(state[1:])
    
    
# 20개씩 출력
for i in range((switch//20)+1):
    if i==(switch//20):
        print(*state[1+20*i:])
    else:
        print(*state[1+20*i:1+20*i+20])
