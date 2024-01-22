# 일단 리스트의 중첩이 되지 않는 총 개수를 구하자 => max = len(set(gems))

# 0번째부터 시작해서 배열에 +1 씩해서 저 max와 같아질때까지 반복문 돌린 후 answer에 append
# ->  0 ~ n 까지를 통해 첫 번째 전체가 나오는 길이의 구간을 알 수 있게 된다.
# gems[0 : max+i ]
# 1번을 예제로 든다면 4개가 다 들어가게 되는 구간은
# ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE" ]이 된다.
# check_len =  7


# 독립적 반복분
# 1번부터는 answer에 있는 길이와 비교한다.
# gems[j : check_len+j ]
# [ "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"] 

## 이 길이에서 4개가 충족된다면 구간에서 -1 씩 진행한다 
## [ "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE" ] 
## => 4개충족
## [ "RUBY", "RUBY", "DIA", "DIA", "EMERALD" ] 
## => 3개 충족
## 끝, answer를 [ "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE" ]  로 바꾼다 ( 인덱스를 저장 )


### 위를 반복
### 근데 인덱스 2 부터 시작하게 된다면 out of range가 뜰 수 있기 때문에 이에대한 적절한 조치 필요해보임
### 끝을 end로 해서 gems[j : check_len+j ] 또는 gems[ j : end ] 로 비교하게 해야할듯


"""
예상결과
1. ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	[3, 7]

0. max = len(set(gems))
-> 4

1-1. 0번째부터 시작해서 배열에 +1 씩해서 저 max와 같아질때까지 반복문 돌린 후 answer에 append
-> ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE" ]
-> check_len = 7


1-2. index 1부터는  answer에 있는 길이와 비교한다.
-> gems[1 : check_len+1 ]
-> [ "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"] 
-> max 과 비교 후 같다면  gems[1 : 7+1-j ] 진행

-> [ "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE" ] 
-> max 과 비교 후 같다면  gems[1 : 7+1-j ] 진행

-> [ "RUBY", "RUBY", "DIA", "DIA", "EMERALD" ] 
-> max 과 비교 후 같지 않기 떄문에 break



1-3. index 2를 1과 같은 방식으로 진행
-> 근데 끝 라인이 out of range가 되지 않게 조건문 걸기


"""


def solution(gems):
    answer = []
    max = len(set(gems))
    print(len(set(gems)))
    for i in range(len(gems)-max+1):
        if len(set(gems[0:max+i])) == max :
            answer.append(gems[0:max+i])
        # print(gems[0:max+i])
    return answer