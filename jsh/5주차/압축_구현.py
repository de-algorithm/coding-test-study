# Lv3
#  [PGS] - 프로그래머스
# 1. A ~ Z 까지 색인이 되어있는 dict를 먼저 만들자

# 2. 반복문을 돌리면서 색인이 있는지 찾아보고 있으면 색인번호를 출력하고 +1 한 word를 새로운 색인으로 추가한다

from collections import defaultdict
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def solution(msg):
    answer = []
    
    
    # 1. A ~ Z 까지 색인이 되어있는 dict를 먼저 만들자
    word = defaultdict(int)
    for i in range(len(alpha)):
        word[alpha[i]] = (i+1)
    
    
    # 2. 반복문을 돌리면서 색인이 있는지 찾아보고 있으면 색인번호를 출력하고 +1 한 word를 새로운 색인으로 추가한다
    while True:
        if msg in word:
            answer.append(word[msg])
            break
        for i in range(1,len(msg)):
            print('-'*20)
            print(f'현재 입력(w) : {msg[:i]}')
            print(f'check : {msg[:i+1]}')
            if msg[:i+1] not in word:
                # print(msg[:i+1])
                answer.append(word[msg[:i]])
                # print(word[msg[:i]])
                print(f'색인추가 : {msg[:i+1]} : {len(word)+1}')
                word[msg[:i+1]] = len(word)+1
                # print('변경 전 : ',msg)
                msg = msg[i:]
                # print('변경 후 : ',msg)
                
                break
    return answer
    
"""
--------------------
현재 입력(w) : K
check : KA
색인추가 : KA : 27
변경 전 :  KAKAO
변경 후 :  AKAO
--------------------
현재 입력(w) : A
check : AK
색인추가 : AK : 28
변경 전 :  AKAO
변경 후 :  KAO
--------------------
현재 입력(w) : K
check : KA
--------------------
현재 입력(w) : KA
check : KAO
색인추가 : KAO : 29
변경 전 :  KAO
변경 후 :  O    
"""


"""
테스트 3
입력값 〉	"ABABABABABABABAB"
기댓값 〉	[1, 2, 27, 29, 28, 31, 30]
실행 결과 〉	테스트를 통과하였습니다.



출력 〉	

--------------------
현재 입력(w) : A
check : AB
색인추가 : AB : 27
변경 전 :  ABABABABABABABAB
변경 후 :  BABABABABABABAB
--------------------
현재 입력(w) : B
check : BA
색인추가 : BA : 28
변경 전 :  BABABABABABABAB
변경 후 :  ABABABABABABAB
--------------------
현재 입력(w) : A
check : AB
--------------------
현재 입력(w) : AB
check : ABA
색인추가 : ABA : 29
변경 전 :  ABABABABABABAB
변경 후 :  ABABABABABAB
--------------------
현재 입력(w) : A
check : AB
--------------------
현재 입력(w) : AB
check : ABA
--------------------
현재 입력(w) : ABA
check : ABAB
색인추가 : ABAB : 30
변경 전 :  ABABABABABAB
변경 후 :  BABABABAB
--------------------
현재 입력(w) : B
check : BA
--------------------
check : BAB
색인추가 : BAB : 31
변경 전 :  BABABABAB
변경 후 :  BABABAB
--------------------
현재 입력(w) : B
check : BA
--------------------
현재 입력(w) : BA
check : BAB
--------------------
현재 입력(w) : BAB
check : BABA
색인추가 : BABA : 32
변경 전 :  BABABAB
변경 후 :  ABAB
"""

    