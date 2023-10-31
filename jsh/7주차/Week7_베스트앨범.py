# 베스트앨범 | LEVEL 3
# 40min

# dic_1 : 총합을 계산하는 dict
# dic_2 : index 와 plays를 list로 넣는 dict

from collections import defaultdict

def solution(genres, plays):
    answer = []
    dic_1 = defaultdict(int)
    dic_2 = defaultdict(list)
    for i in range(len(genres)):
        # i : index  값
        if genres[i] not in dic_1 :
            dic_1[genres[i]] = plays[i]
        else :
            dic_1[genres[i]] += plays[i]
    # defaultdict(<class 'int'>, {'classic': 1450, 'pop': 3100})

    for j in range(len(genres)):
        dic_2[genres[j]].append([j,plays[j]])
    # defaultdict(<class 'list'>, {'classic': [[0, 500], [2, 150], [3, 800]], 'pop': [[1, 600], [4, 2500]]})
    
    
    
    
    for item,sum in sorted(dic_1.items(),key=lambda x:x[1], reverse = True) :
        # [('pop', 3100), ('classic', 1450)]

        for idx,val in sorted(dic_2[item], key=lambda x:x[1] , reverse = True)[:2]:
            # print(idx)
            answer.append(idx)
    
    
    
    return answer

