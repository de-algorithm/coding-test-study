# 특정구간의 보석 종류별로 적어도 1개 이상 구매
# 구간에 있는것은 다 구매해야함
# 위에 조건으로 가장 짧은 구간 찾기
# return = 진열대 [시작번호,끝번호] / 여러개라면 시작 진열대 번호가 가장 작은 것

import collections

def solution(gems):
    # 보석 종류 구하기
    num = len(set(gems))
    answer = []

    left = 0
    # 보석 카운팅 사전 초기화
    counter = collections.Counter()
    
    for right in range(len(gems)):
        # 보석 카운팅
        counter[gems[right]] += 1
        right += 1
        
        # 보석 종류가 모두 사전에 있을 경우
        while len(counter) == num:
            # 왼쪽부터 보석 제거
            counter[gems[left]] -= 1
            if counter[gems[left]] == 0:
                del counter[gems[left]]
            left += 1
            # 모두 사전에 있는 구간 저장
            answer.append([left, right])
    
    # 가장 짧은 구간, 시작이 작은 순으로 정렬
    return sorted(answer, key = lambda x: (x[1]-x[0], x[0]))[0]