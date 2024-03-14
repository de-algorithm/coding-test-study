from heapq import heapify, heappop, heappush


def solution(files: list[int]) -> int:
    """
    두 개의 파일을 합쳐서 하나의 임시파일을 만들고 
    계속 두개 씩 합쳐서 최종적으로 하나의 파일을 만든다.
    합치는 필요 비용이 두 파일 크기의 합이라고 가정할 때, 필요한 최소비용을 찾기.
    
    가장 코스트가 낮은 파일들끼리 합쳐서 최종 파일을 만든다.
    - heapq 사용해서 heap sort되도록 함
    - pop하면 가장 코스트가 낮은 element를 리턴한다.
    - files 길이가 1개가 될때 까지 두개를 pop해서 합친 값을 다시 push 한다.
        - 가장 코스트가 낮은 두개를 합친 값은 answer에 계속 추가한다.
    - answer을 반환한다.

    Args:
        files (list[int]): 수록한 파일의 크기 K개 (3 ≤ K ≤ 1,000,000)

    Returns:
        int: 모든 장을 합치는데 필요한 최소비용
    """
    answer = 0
    heapify(files)
    while len(files) > 1:
        first_low = heappop(files)
        sec_low = heappop(files)
        file_concat_cost = first_low + sec_low
        answer += file_concat_cost
        heappush(files, file_concat_cost)
    return answer