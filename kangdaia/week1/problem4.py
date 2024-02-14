from collections import deque


def solution(begin: str, target: str, words: list[str]) -> int:
    """프로그래머스 단어변환 레벨 3
    1. 한번에 한개의 알파벳만 바꿀 수 있음
    2. words안에 있는 단어로만 변환할 수 있음
    두가지 조건을 지켜서 begin을 target으로 변환시킬 때,
    가장 빠른 과정의 변환 횟수를 구함.

    만약 target이 words 목록에 없으면 변환이 불가능 하므로, 0을 반환
    아니면, bfs function을 통해 과정 횟수 구함.

    Args:
        begin (str): 시작하는 단어
        target (str): 마지막 변환할 단어
        words (list[str]): 변환에 사용가능한 단어목록

    Returns:
        int: 가장 빠른 변환 과정의 횟수
    """
    if target not in words:
        return 0
    return bfs(begin, target, words)


def bfs(begin: str, target: str, words: list[str]) -> int:
    """
    solution의 helper function
    deque를 이용해, 각 단어의 변환 횟수를 추적한다.

    queue가 빌 때 까지,
    - 현재 단어가 target과 동일한지 확인 -> 동일하면 loop end
    - 단어 목록을 돌면서, 각 단어의 알파벳을 현재 단어와 비교하며,
        1회 변환으로 도달 가능한 단어인지 확인.
    - 1회 변환으로 가능한 단어면 큐에 추가한다.

    Args:
        begin (str): 시작하는 단어
        target (str): 마지막 변환할 단어
        words (list[str]): 변환에 사용가능한 단어목록

    Returns:
        int: 가장 빠른 변환 과정의 횟수
    """
    queue = deque()
    queue.append([begin, 0])
    result = 0
    while queue:
        curr_word, step = queue.popleft()

        if curr_word == target:
            result = step
            break

        for word in words:
            count = 0
            for i in range(len(curr_word)):
                if curr_word[i] != word[i]:
                    count += 1
            if count == 1:
                queue.append([word, step + 1])
    return result
