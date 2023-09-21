'''
Date        : 2023.09.20
Problem     : https://school.programmers.co.kr/learn/courses/30/lessons/43163
Tag         : BFS
'''
from collections import deque
def solution(begin, target, words):
    
    # target이 words안에 없는 경우
    if target not in words:
        return 0
    
    # 인접 리스트 만들기
    words.append(begin)
    len_words = len(words)
    graph = [[] for _ in range(len_words)]
    
    for i in range(len_words):
        graph[i] = find(words[i], words)
        
    # print(graph)
    
    visited = [False]*len_words
    begin_idx = len_words-1
    q = deque()
    q.append((begin_idx, 0))
    visited[begin_idx] = True

    while q:
        curr_idx, count = q.popleft()
        
        if words[curr_idx] == target:
            return count
    
        for neighboor_idx in graph[curr_idx]:
            if not visited[neighboor_idx]:
                visited[neighboor_idx] = True
                q.append((neighboor_idx, count+1))   
    return 0 
    
# 1개의 알파벳만 다른 단어들을 리스트로 반환하는 함수 
def find(word1, words):
    result = []
    
    for i in range(len(words)):
        count = 0
        for j in range(len(word1)):
            if word1[j] != words[i][j]:
                count+=1
        if count == 1:
            result.append(i)
    return result