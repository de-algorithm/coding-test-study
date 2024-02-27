# 오리 녹음소리를 듣고 몇마리인지 판별하기
# quack 순서로 반복되지 않은 소리 = 오리의 수
# 올바르지 않을 경우 -1 반환

# 올바르지 않은 경우
# 1.문자열 길이가 5의 배수 x
# 2.quack 순서가 올바르지 않음
# 3.오리가 없을 때

sound = input()
visited = [0] * len(sound)
cnt = 0

if len(sound) % 5 != 0:
    print(-1)
    exit()


def solve(start):
    global cnt
    quack = 'quack'
    j = 0
    first = True
    for i in range(start, len(sound)):
        if sound[i] == quack[j] and not visited[i]:
            visited[i] = True
            if sound[i] == 'k':
                if first:
                    cnt += 1
                    first = False
                j = 0
                continue
            j += 1


for i in range(len(sound)):
    if sound[i] == 'q' and not visited[i]:
        solve(i)

if not all(visited) or cnt == 0:
    print(-1)
else:
    print(cnt)