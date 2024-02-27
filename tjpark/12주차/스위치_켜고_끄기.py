# 학생은 성별과 받은 자연 수에 따라 스위치를 조작
# 받은 수는 1 ~ 스위치 총 개수

# 남학생: 스위치 번호가 받은 수의 배수 = 스위치 변경
# 여학생: 받은 수의 스위치를 중심으로 좌우 대칭 & 가장 많은 스위치를 포함하는 구간(항상 홀수) = 해당 구간 모두 변경
# 좌우대칭이 아니면 받은 수 스위치만 변경

def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return

N = int(input())
switch = [-1] + list(map(int, input().split()))
students = int(input())
for _ in range(students):
    sex, num = map(int, input().split())
    # 남자
    if sex == 1:
        for i in range(num, N+1, num):
            change(i)
    # 여자
    else:
        change(num)
        for k in range(N//2):
            if num + k > N or num - k < 1 : break
            if switch[num + k] == switch[num - k]:
                change(num + k)
                change(num - k)
            else:
                break
                
for i in range(1, N+1):
    print(switch[i], end = " ")
    if i % 20 == 0 :
        print()

