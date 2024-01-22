# start > 12:15
# end > 12:22


# Gold 5
# 사람들까지의 거리의 합이 최소 
# -> 사람들의 중간이 가장 최소가 되지 않을까?

## 전체 사람 수 구하기 ( all_num )
## 0부터시작해서 (2/전체사람수) 가 될 때 까지 반복문 돌려보기


n = int(input())
all_num = 0
all_list = []
for i in range(n):
    x,a = map(int,input().split())
    all_list.append([x,a])
    all_num += a

# sort 안해서 한 번 실패. 실패 후 넣었더니 성공
all_list.sort(key = lambda x : x[0])

cur_people = 0
for i in range(n):
    cur_people+= all_list[i][1]
    if cur_people >= all_num/2 :
        print(all_list[i][0])
        break
    
    