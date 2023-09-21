# Lv.3

# 13:30 시작
# 13:54 끝

#1. 우선 문장 을 비교해서 한 개의알파벳만 바꿀 수 있는지 조건을 주자
#1
# for i in range(len(begin)):
#     if begin[i] != target[i]:
#         cnt_change += 1

#2. "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계 처럼 바꾸는걸 구현해보자
# deque에 ( cnt_change,current_word, [남은 words]) 를 넣자

from collections import deque

def solution(begin, target, words):
    len_string = len(begin)
    que = deque()
    count = 0
    que.append((count,begin, words))
    
    while(que):
        count, current_word, words = que.popleft()
        # print(count, current_word, words)
        if current_word == target :
                return count
        for check_word in words :
            cnt_change = 0
            for i in range(len_string):
                if current_word[i] != check_word[i]:
                    cnt_change += 1
            if cnt_change == 1 :
                words.remove(check_word)
                que.append((count+1,check_word, words))
    return 0



# 채점을 시작합니다.
# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.10ms, 10.4MB)
# 테스트 3 〉	통과 (0.36ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0