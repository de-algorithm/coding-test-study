# k개의 문자열을 포함하는 문자열 기준
# 최소, 최대 길이 출력
# 조건에 부합하지 않으면 -1 출력

import sys
from collections import defaultdict

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    w = input().rstrip()
    k = int(input())

    # 각 문자의 개수를 세는 딕셔너리
    count_char_dict = defaultdict(int)

    # 각 문자의 개수 세기
    for char in w:
        count_char_dict[char] += 1

    # 결과와 관련된 변수
    check = False
    max_answer = -1
    min_answer = len(w)

    # 특정 문자열의 위치 index를 저장하는 딕셔너리
    check_dict = {}

    # 모든 문자열에 대해서
    for i in range(len(w)):
        # 해당 문자열이 k개 이하이면 다음 문자
        if count_char_dict[w[i]] < k:
            continue

        # k개 이상인 문자를 찾으면 정답이 있음
        check = True
        # 해당 문자열을 key로하고 index리스트를 value로 갖는 딕셔너리
        check_dict[w[i]] = check_dict.get(w[i], []) + [i]
    #print(check_dict)
    # 딕셔너리를 돌면서
    for key, value_list in check_dict.items():
        # 인덱스 번호를 바탕으로
        for i in range(len(value_list) - k + 1):
            # 최대 최소 갱신
            max_answer = max(max_answer, value_list[i+k-1] - value_list[i] +1)
            min_answer = min(min_answer, value_list[i + k - 1] - value_list[i] + 1)

    # 정답이 있으면 출력
    if check:
        print(min_answer, max_answer)

    # 없으면 -1출력
    else:
        print(-1)