# 기차에 일렬로 20개 좌석이 있음
# 기차에 명령이 내려짐
# 1 i x: i번째 기차에 x번째 좌석에 사람을 태워라 / 이미 있으면 행동 x
# 2 i x: i기차, x좌석 사람 하차 / 없으면 행동 x
# 3 i: i기차 모두 한칸씩 뒤로 / 20번에 사람 있으면 하차
# 4 i: i기차 모두 한칸씩 앞으로 / 1번에 사람 있으면 하차
# 중복된 승객 순서가 있는 기차는 은하수를 건널 수 없다.
# return: 은하수를 건널 수 있는 기차 수 출력

# 81%에서 계속 실패함
# 반례를 모르겠음 ㅠㅠ
import sys
from collections import deque


N, M = map(int,sys.stdin.readline().split())

order_list = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]

init_value = deque([0] * 20)
train = [deque([0] * 20) for _ in range(N)]

# 후보군
train_set = set()
# 중복된 기차를 어떻게 빨리 찾아낼 것인지
for order in order_list:

    if len(order) == 3:
        o, i, x = order
        i += -1
        x += -1
    else:
        o, i = order
        i += -1

    if o == 1:
        train[i][x] = 1
        train_set.add(i)
    elif o == 2:
        train[i][x] = 0
    elif o == 3:
        train[i].pop()
        train[i].appendleft(0)
    elif o == 4:
        train[i].popleft()
        train[i].append(0)
    
    if o != 1:
        if train[i] == init_value:
            train_set.discard(i)


tr_candiates = [train[i] for i in train_set]

tr_dist = set([tuple(tr) for tr in tr_candiates])
tr_cnt = len(tr_dist)

if tr_cnt < N:
    tr_cnt += 1
for i in train:
    print(i)

print(tr_cnt)
