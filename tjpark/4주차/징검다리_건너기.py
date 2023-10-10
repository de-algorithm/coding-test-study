# 문제설명
# 디딤돌의 숫자는 한 번 밟을 때 마다 1씩 줄어듬
# 0이면 k만큼 건너 뛸 수 있음
# stones 길이 10만, 각 원소 최대 2억

# Binary search 풀이 (360 ms 이하)
# mid = 건널 수 있는 횟수
# 각 구간별로 최대로 건널 수 있는 횟수(mid) 구하기
def solution(stones, k):
    answer = 0
    stone_set = sorted(set(stones))
    # 최소, 최댓값 구하기
    start, end = stone_set[0], stone_set[-1]
    
    while start <= end:
        # mid = 건널 수 있는 횟수
        mid = (start+end) // 2
        # cnt = mid번 건널 때 연속으로 못건너는 돌다리 count
        cnt = 0
        
        
        # 건널 수 있는 횟수가 k번 연속 mid 이하인 경우를 찾음
        # 연속된 구간에서 최대 건널 수 있는 길이 'k'
        # k길이 만큼의 구간에서
        # mid번 건널 때 mid이하면 cnt+1을 하게되는데
        # cnt가 k보다 같거나 크면 못건너게 됨
        for stone in stones:
            if cnt < k:
                if stone <= mid:
                    cnt += 1
                else:
                    cnt = 0
            else:
                break
        
        # mid번 건너기 가능할 경우
        # mid보다 더 건널 수 있는지 확인
        if cnt < k:
            start = mid+1
        # mid번 건너기 불가능할 경우
        # mid보다 더 적게 건널 수 있는지 확인
        else:
            answer = mid
            end = mid-1          

    return answer


# window sliding maximum 풀이
# 즉, k구간 원소 최대값 = k구간 건널 수 있는 최대 횟수
# 1. 구간 별 최대값을 통해 건널 수 있는 횟수를 구함
# 2. 그 중 최소 = 징검다리 건널 수 있는 최대 인원
# 시간 초과
# def solution(stones, k):
#     answer = max(stones)
#     for i in range(len(stones)):
        
#         if i+k > len(stones):
#             break
#         answer = min(answer, (max(stones[i:i+k])))
    
#     return answer