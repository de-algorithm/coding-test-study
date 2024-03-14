def solution(stones: list[int], k: int) -> int:
    """
    중간값보다 작은 발판 수가 연속되는 횟수를 카운트해서 그 리스트의 최대값을 체크
    최대값을 k랑 비교

    Args:
        stones (list[int]): 밟을 수 있는 횟수가 포함된 징검다리 배열
        k (int): 한번에 건널 수 있는 최대 징검다리 수

    Returns:
        int: 징검다리를 건널 수 있는 최대 인원
    """
    i, j = min(stones), max(stones)
    answer = 0
    if i == j:
        return i
    while i <= j:
        mid = (i+j)//2
        repet, count = [], 0
        for stone in stones:
            if stone <= mid:
                count += 1
            else:
                repet.append(count)
                count = 0
        else:
            repet.append(count)
            max_con = max(repet)
        if max_con < k:
            i = mid+1
        else:
            answer = max(mid, answer)
            j = mid-1
    return answer
