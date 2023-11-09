# return= genre별 가장 많이 재생된 노래 두 개씩 출력

# 1. 장르 별 전체 재생 수 높은 순으로 
# 2. 해당 장르의 노래에 재생 수 높은 순으로
# 3. 재생 수 같을 시 노래 번호 낮은 순으로 
# 4. 장르별 최대 2개 출력
from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    # dic = 장르, 노래별 재생 수
    # total_dic = 장르 별 전체 재생 수
    dic = defaultdict(dict)
    total_dic = defaultdict(int)
    
    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        dic[genre][i] = play
        
        total_dic[genre] += play

    # 장르 전체 재생횟수 큰 수 부터 정렬
    total_dic_item = list(total_dic.items())
    total_dic_item.sort(key = lambda x: x[1], reverse=True)
    
    # 장르별 전체 재생횟수 큰 순으로
    # 노래 재생횟수 큰거 최대 2개 추출
    for key, _ in total_dic_item:
        dic_item = list(dic[key].items())
        dic_item.sort(key = lambda x: (x[1], -x[0]), reverse=True)
        
        if len(dic_item) < 2:
            answer.append(dic_item[0][0])
        else:
            answer.append(dic_item[0][0])
            answer.append(dic_item[1][0])
    #print(answer)
    return answer