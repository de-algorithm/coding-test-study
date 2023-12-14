'''
**string 자료형은 immutable type이라 수정할 수 없다. 

반례
- record 문자열 개수가 5의 배수가 아닐 때 (울다 만 오리가 있는 경우)

'''
import sys
from collections import Counter
sys.stdin = open('yunji/input.txt', 'r')

input = sys.stdin.readline
record = input()


def f(record):
    sound = 'quack'
    count = 0   # 오리 마리 수 
    
    # 울다 만 오리가 있을 때 
    if not len(record) % 5 == 0:
        return -1

    # 울음소리 짝이 안 맞을때
    # if not len(set(Counter(record).values())):
    #     return -1

    for _ in range(len(record)//5):    # 최대 오리 수만큼 반복 
        i = 0 # i : sound 인덱스
        for j in range(len(record)):    # j : record 인덱스 / 한 오리가 낸 울음소리를 찾기 위한 반복문 
            if sound[i] == record[j]:   # 올바른 울음소리라면 해당 문자는 '_' 처리하여 record에서 제거
                if j == 0:              # record에서 첫 문자일 경우 
                    record = '_' + record[j+1:]
                elif j == len(record)-1:    # record에서 첫, 마지막 문자를 제외한 중간 문자일 경우
                    record = record[:j] + '_'
                else:                       # record에서 마지막 문자일 경우
                    record = record[:j] + '_' + record[j+1:]
            
                i += 1  # 울음소리 순서 인덱스 증가
            if i == 5:    # 한 오리가 울음소리를 반복할 수 있기에 다시 첫 인덱스로 초기화
                i = 0
        
        # record 한바퀴 돌고 난 후 
        if record.count('_') % 5 == 0:
            count += 1  # 오리 마리 수 증가
        print(record)
        print(count)
        if set(record)=={'_'}:
            break
        
    if not set(record)=={'_'}:
        count = -1
        
    return count

print(f(record))