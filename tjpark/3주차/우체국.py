# 일직선 상에 마을이 있음
# 각 사람들까지의 거리의 합이 최소가 되는 위치에 우체국을 세움
# 거리 * 사람 수 합이 최소가 되어야함
# 시간초과로 다 구할 수 없음 (1억 * 1억), 최적의 해를 구하는 방법을 찾아야함
import sys
#import time

N = int(sys.stdin.readline())
town_list = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
town_list.sort(key= lambda x: x[0])

#start_time = time.time()

total_people = sum(i[1] for i in town_list)
cnt = 0

# 사람이 절반 이상이 될 때 최소합이 됨
for town, people in town_list:
    cnt += people
    if cnt >= total_people/2:
        print(town)
        break


'''
# 시간초과 code
def cal(place ,town_li):
    distance = 0
    for X, A in town_li:
        if place != X:
            distance += abs(place-X) * A
    
    return distance


# 가운데에서 시작
center = len(town_list)//2
find = True

direct = -1
move = 0
min_val = cal(center, town_list)
place = center

while True:
    move += 1
    cal_val = 0
    # 리스트 모두 돌았을 때 종료
    if (direct == 0 and center - move < 0) or \
        (direct == 1 and center + move > len(town_list)) or \
        (direct == -1 and (center - move < 0 or center + move > len(town_list))):
        print(place)
        break

    # 왼쪽으로 갈지 오른쪽으로 갈지 선택
    if direct == -1 :
        left = cal(center-move,town_list)
        right = cal(center+move,town_list)
        if left < right:
            direct = 0
            cal_val = left
            cal_place = center - move
        elif right < left:
            direct = 1
            cal_val = right
            cal_place = center + move
        else:
            cal_val = left
            cal_place = center - move

    # 왼쪽
    elif direct == 0:
        cal_place = center - move
        cal_val = cal(place,town_list)
    # 오른쪽
    else:
        cal_place = center + move
        cal_val = cal(place, town_list)

    # 계산한 값이 커지면 이전 값이 최소 값으로 간주
    if cal_val > min_val:
        print(place)
        break
    else:
        min_val = cal_val
        place = cal_place
'''


#end_time = time.time()
#execution_time = end_time - start_time
#print(execution_time)
