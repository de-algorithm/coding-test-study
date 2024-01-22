# Silver 2

## start > 12 : 50
## end > 13:40

# 기차는 20개의 일렬로 된 좌석이 있고, 한 개의 좌석에는 한 명의 사람이 탈 수 있다. 
# 1. > n X 20개의 빈 리스트 ( 0 으로 초기화 된 ) 생성


# 2. m개의 명령을 수행
# order_list[0] == 1
# -> all_train[order_list[1]][order_list[2]] = 1

# order_list[0] == 2
# -> all_train[order_list[1]][order_list[2]] = 0

# order_list[0] ==- 3
# -> for i in range(19,0,-1):
# ->    all_train[order_list[1]-1][i] = all_train[order_list[1]-1][i-1]
# -> all_train[order_list[1]-1][0] = 0

# order_list[0] == 4
# -> for i in range(19):
# ->    all_train[order_list[1]-1][i] = all_train[order_list[1]-1][i+1]
# -> all_train[order_list[1]-1][-1] = 0


# 3. check_list를 통해 중복제거 ( not in 구문 활용 )


# 1.
n, m = map(int, input().split())
all_train = [[0 for _ in range(20)] for _ in range(n)]

# 2.
for _ in range(m):
    order_list = list(map(int , input().split()))
    if order_list[0] == 1:
        all_train[order_list[1]-1][order_list[2]-1] = 1
    elif order_list[0] == 2:
        all_train[order_list[1]-1][order_list[2]-1] = 0
    elif order_list[0] == 3:
        for i in range(19,0,-1):
            all_train[order_list[1]-1][i] = all_train[order_list[1]-1][i-1]
        all_train[order_list[1]-1][0] = 0
        
    elif order_list[0] == 4:
        for i in range(19):
            all_train[order_list[1]-1][i] = all_train[order_list[1]-1][i+1]
        all_train[order_list[1]-1][-1] = 0


# 3.
check_list = []
cnt = 0
for i in range(n):
    if all_train[i] not in check_list:
        check_list.append(all_train[i])
        cnt += 1

print(cnt)
