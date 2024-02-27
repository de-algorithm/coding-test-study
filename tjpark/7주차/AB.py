# 집합 A,B에 문자열 S를 추가/삭제 기능 
# add A S = A집합에 S추가
# delete A S =  A에서 S제거
# find S: A원소의 접두사와 B원소 접미사를 붙여 S가 되는 경우의 수 반환

import sys
from collections import defaultdict

# 접두, 접미 합칠 때 효율적인 방법
# 1.접미/접두 모든 경우의 수를 check = 비효율
# 2.dp를 사용해 이미 체크한 값을 사용한다.
# A와 B에 주어지는 문자열과 find에서 주어지는 문자는 모두

# 계산 방법
# 접미사의 길이가 낮은 순으로 경우의 수 계산 진행
# 접미사의 길이가
# 알파벳 길이가 길때 낮은 길이의 알파벳이 몇개 까지 가능했는지 더하기
# dp로 진행
def string_find(dic, find_string):
    print('find '+find_string)
    result = 0
    dic_key = list(dic['A'].keys())
    dic_key.sort(key= lambda x: len(x))

    check_dic = defaultdict(int)
    check = []
    for st_a in dic_key:
        
        check = 0
        # 해당 접두사의 문자 하나씩 왼쪽으로 이동해 계산했는지 확인
        for i in range(len(st_a),0,-1):
            st_cut = st_a[:i]
            #print(st_a)
            #print(i, st_a[:i])
            if st_cut in check_dic:
                #result += check_dic[st_cut]
                check_dic[st_a] += check_dic[st_cut]
                check = i
                break
        
        # 어디까지 체크했는지 확인 후 체크안된 곳 부터 계산 시작
        # A를 자를 때 다음 올 수 있는 문자가 B의 뒷부분인 경우 찾기
        for i in range(check, len(st_a),1):
            
            # 뒷문자
            find_string_cut_back = find_string[i+1:]
            # 앞문자
            find_string_cut_front = find_string[:i+1]
            
            print('cut '+find_string_cut_front, find_string_cut_back)
            # 찾아야하는 문자 기준, 접미사의 뒷문자에 포함되어 있는지 
            for j in dic['B']:
                idx = len(find_string_cut_back)
                #print('접두사 '+j)
                print('comp '+find_string_cut_back, j[-idx:])
                if len(find_string_cut_back) <= len(j) and \
                    j[-idx:] == find_string_cut_back :
                    check_dic[find_string_cut_front] += 1
        print(check_dic)
    #print(check_dic)
    print(sum(check_dic.values()))

N = int(sys.stdin.readline())
dic = defaultdict(dict)


for _ in range(N):
    q = sys.stdin.readline().split()

    if q[0] == 'add':
        agg, string = q[1], q[2]

        if string not in dic[agg]:
            dic[agg][string] = 1
        else:
            dic[agg][string] += 1
    
    elif q[0] == 'delete':
        agg, string = q[1], q[2]

        dic[agg][string] -= 1

        if dic[agg][string] == 0:
            del dic[agg][string]
    
    else:
        string_find(dic,q[1])
        # for st_a in dic['A']:

        #     st_find = q[1]
        #     if st_a == st_find:


'''
a bcd 
ab cd
a(b-) bcd 
ab (b-)cd
'''

'''
target = abcd
a = abcd b= abcd, cd
a(bcd-) (a-)bcd
ab(cd-) (ab-)cd
ab(cd-) cd
abc(d-) (abc-)d
abc(d-) (c-)d
'''
