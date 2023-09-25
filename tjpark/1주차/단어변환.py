# 시작 단어를 타겟 단어로 변경하는 가장 짧은 단계 수 구하기
# 한번에 하나의 알파벳만 변경 가능
# words에 있는 단어로만 변환 가능
# 변환 할 수 없을 땐 0 반환

from collections import deque

def solution(begin, target, words):
    answer = 0
    
    # 이미 비교한 단어 저장
    visited = [1] * len(words)
    # bfs를 위한 deque
    que = deque([[begin,0]])
    
    while que:
        
        # 기준 단어와 변경한 단계 수 가지고오기 
        std_word, step = que.popleft()
        
        # 기준단어와 목표단어가 같으면 단계 수 반환
        if std_word == target:
            return step
        
        for i in range(len(words)):
            # 해당 단어를 비교한 적있는지 확인
            if visited[i]:
                
                # 다른 알파벳 하나만 있는 단어 찾기
                diff = 0
                for j in range(len(std_word)):     
                    if std_word[j] != words[i][j]:
                        diff += 1
                        
                    if diff > 2:
                        break
                
                # 찾은 단어 저장 및 방문 기록
                if diff == 1:
                    que.append([words[i], step+1])
                    visited[i] += -1
    
    return 0
