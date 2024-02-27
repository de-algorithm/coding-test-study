def solution(genres, plays):
    answer = []
    dic1 = {} # index, plays 기록
    dic2 = {} # 많이 재생된 장르 기록
    
    for idx, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(idx, p)]
        else:
            dic1[g].append((idx, p))
        
        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p
    
    for genre, _ in sorted(dic2.items(), key = lambda x : x[1], reverse=True):
        for index, _ in sorted(dic1[genre], key = lambda x : x[1], reverse = True)[:2]:
            answer.append(index)
    return answer