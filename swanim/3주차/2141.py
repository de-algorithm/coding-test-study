n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
#ls.sort(key = lambda x : (-x[1], x[0]))

# 마을 사람 총합 구하기
population = 0
for i in ls:
    population += i[1]

# 절반 넘어가는 마을 찾기
ls.sort()
tmp = 0
for i in ls:
    tmp += i[1]
    if tmp >= population / 2:
        print(i[0])
        break