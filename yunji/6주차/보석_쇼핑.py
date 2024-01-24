

from collections import defaultdict
def solution(gems):
    answer = []
    gems_dict = defaultdict(int)                    # {보석 종류 : 개수}

    interval_len= len(gems) +1                      # 최단 구간 길이
    start, end = 0, 0                               # 구간 시작 번호, 끝 번호
    check_len = len(set(gems))                      # 보석의 총 종류 수
    
    while end < len(gems):                          # 구간 끝 번호가 진열대 끝까지 갈 동안 
        gems_dict[gems[end]] += 1                   # 해당 보석의 개수 추가
        end += 1                                    # 끝 번호 증가
        
        if len(gems_dict) == check_len:             # 모든 종류의 보석을 포함하는 구간
            while start < end:                      # 시작 번호 증가시키며 최단 구간 탐색
                if gems_dict[gems[start]] > 1:      # 시작번호에 해당하는 보석이 구간 내에 하나 이상 있을 때
                    gems_dict[gems[start]] -= 1     # 구간 내 보석 1개 빼기 
                    start+=1                        # 시작번호 증가
                elif interval_len > end - start:    # 기존의 최단 구간 거리보다 현재의 구간거리가 더 짧다면
                    interval_len = end - start      # 최단 구간 거리 갱신
                    answer = [start+1, end]         # answer 갱신
                    break                           
                else:
                    break
    return answer


'''
반례
["A","B","B","B","B","B","B","C","B","A"] [8,10]
["A", "B", "C", "B", "F", "D", "A", "F", "B", "D", "B"] [3, 7]
'''