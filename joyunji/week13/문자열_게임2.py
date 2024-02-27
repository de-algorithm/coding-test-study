import sys
from collections import defaultdict
sys.stdin = open('yunji/input.txt', 'r')

input = sys.stdin.readline

T = int(input())    # 문자열 게임의 수
for _ in range(T):
    W = input().rstrip('\n')
    K = int(input())

    # {'s': [0, [0]], 'u': [1, [1, 7]],...} / {문자: [count,[문자 인덱스,..,]]}
    dic = defaultdict(list)
    answer = []
    for i in range(len(W)):
        # count값이 없으면 추가 후 인덱스 값도 추가
        if not dic[W[i]]:
            dic[W[i]].append(1) # 카운트 초기화 
            dic[W[i]].append([i])
        else:
            dic[W[i]][0] += 1   # 카운트 증가
            dic[W[i]][1].append(i)
        count = dic[W[i]][0]
        if count >= K:   # 해당 문자의 개수가 K개보다 크거나 같을 때 
            # 문자열 길이 = dic[W[i]][1] 리스트에서 마지막 원소-(count-K)번째 원소+1 
            answer.append(dic[W[i]][1][-1]-dic[W[i]][1][count-K]+1)
        
    if answer:
        answer.sort()
        print(answer[0], answer[-1])
    else:
        print(-1)