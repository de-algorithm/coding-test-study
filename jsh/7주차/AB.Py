# 27652번 AB | 골드 1
# 시간 : 2704ms
# 걸린시간 : 1h?
## 구상 : 40min
## 구현 : 20min
"""
    7
    add A aba
    => A {
        a : 1
        ab : 1
        aba : 1
    }
    add A a
    => A {
        a : 2
        ab : 1
        aba : 1
    }
    add A ab
    => A{
        a: 3
        ab : 2
        aba : 1
    }
    add B bab
    => B {
        b : 1
        ab : 1
        bab : 1
    }
    add B b
    => B {
        b : 2
        ab : 1
        bab : 1
    }
    add B ab
    => B {
        b : 3
        ab : 2
        bab : 1
    }
    find abab
    => 최종 
    B { b : 3, ab : 2, bab : 1 }
    A{ a: 3, ab : 2, aba : 1 }
    를 통해 
    A에서 하나를 가져간 후 남은 원소가 B에 있는지 파악 후 연산 시작 
    ex) A에서 'a' 를 가져가면 'bab'가 B에 있는지 파악 후 있으면 'a'의 수 * 'bab'의 수 => 3 * 1 = 3
        A에서 'ab' 를 가져가면 'ab'가 B에 있는지 파악 후 있으면 'ab'의 수 * 'ab'의 수 => 2 * 2 = 4
        A에서 'aba' 를 가져가면 'b'가 B에 있는지 파악 후 있으면 'aba'의 수 * 'b'의 수 => 1 * 3 = 3
        3 + 4 + 3 = 10
"""


def add_a(word):
    for i in range(1,len(word)+1):
        # print(word[:i])
        if word[:i] not in A :
            A[word[:i]] = 1
        else :
            A[word[:i]] += 1
        
        # print(f'dict_A : {A}')
        # print('-'*20)

def add_b(word):
    for i in range(1,len(word)+1):
        # print(word[-i:])
        if word[-i:] not in B :
            B[word[-i:]] = 1
        else :
            B[word[-i:]] += 1
        
        # print(f'dict_B : {B}')
        # print('-'*20)


def del_a(word):
    for i in range(1,len(word)+1):
        # print(word[:i])
        if word[:i] not in A :
            A[word[:i]] = 0
        else :
            A[word[:i]] -= 1
        
        # print(f'dict_A : {A}')
        # print('-'*20)

def del_b(word):
    for i in range(1,len(word)+1):
        # print(word[-i:])
        if word[-i:] not in B :
            B[word[-i:]] = 0
        else :
            B[word[-i:]] -= 1
        
        # print(f'dict_B : {B}')
        # print('-'*20)

        
def find(str):
    count = 0
    for item in A:
        if str.find(item) == 0 and str[len(item):] in B :
            # print(f'찾았다! A:  {item},  B : {str.lstrip(item)}')
            # print(f'계산한다! A:  {A[item]} * B : {B[str[len(item):]]} =  {A[item] * B[str[len(item):]]}')
            count += A[item] * B[str[len(item):]]
    print(count)


def solution():
    global A, B
    # 1. 명령 줄 수를 받아온다
    num_line = int(input())
    A = {}
    B = {}
    # 2.
    for _ in range(num_line):
        order_list = list(input().split())
        if order_list[0] == 'add' :
            if order_list[1] == 'A':
                add_a(order_list[2])
            else :
                add_b(order_list[2])
        elif order_list[0] == 'delete' :
            if order_list[1] == 'A':
                del_a(order_list[2])
            else :
                del_b(order_list[2])
        elif order_list[0] == 'find' :
            find(order_list[1])   
            


if __name__ == '__main__':
    solution()
    
    
    
    
"""
예제 1번

A = {}
B = {}

add_a('aba')
add_a('a')
add_a('ab')
add_b('bab')
add_b('b')
add_b('ab')
find('abab')

=>
a
dict_A : {'a': 1}
--------------------
ab
dict_A : {'a': 1, 'ab': 1}
--------------------
aba
dict_A : {'a': 1, 'ab': 1, 'aba': 1}
--------------------
a
dict_A : {'a': 2, 'ab': 1, 'aba': 1}
--------------------
a
dict_A : {'a': 3, 'ab': 1, 'aba': 1}
--------------------
ab
dict_A : {'a': 3, 'ab': 2, 'aba': 1}
--------------------
b
dict_B : {'b': 1}
--------------------
ab
dict_B : {'b': 1, 'ab': 1}
--------------------
bab
dict_B : {'b': 1, 'ab': 1, 'bab': 1}
--------------------
b
dict_B : {'b': 2, 'ab': 1, 'bab': 1}
--------------------
b
dict_B : {'b': 3, 'ab': 1, 'bab': 1}
--------------------
ab
dict_B : {'b': 3, 'ab': 2, 'bab': 1}
--------------------
찾았다! A:  a,  B : bab
계산한다! A:  3 * B : 1 =  3
찾았다! A:  ab,  B : 
계산한다! A:  2 * B : 2 =  4
찾았다! A:  aba,  B : 
계산한다! A:  1 * B : 3 =  3
10

"""



"""
예제 2번

A = {}
B = {}

add_a('a')
add_b('bcd')
add_a('ab')
add_b('cd')
find('abcd')
del_a('a')
del_b('bcd')
find('abcd')



a
dict_A : {'a': 1}
--------------------
d
dict_B : {'d': 1}
--------------------
cd
dict_B : {'d': 1, 'cd': 1}
--------------------
bcd
dict_B : {'d': 1, 'cd': 1, 'bcd': 1}
--------------------
a
dict_A : {'a': 2}
--------------------
ab
dict_A : {'a': 2, 'ab': 1}
--------------------
d
dict_B : {'d': 2, 'cd': 1, 'bcd': 1}
--------------------
cd
dict_B : {'d': 2, 'cd': 2, 'bcd': 1}
--------------------
찾았다! A:  a,  B : bcd
계산한다! A:  2 * B : 1 =  2
찾았다! A:  ab,  B : cd
계산한다! A:  1 * B : 2 =  2
4
a
dict_A : {'a': 1, 'ab': 1}
--------------------
d
dict_B : {'d': 1, 'cd': 2, 'bcd': 1}
--------------------
cd
dict_B : {'d': 1, 'cd': 1, 'bcd': 1}
--------------------
bcd
dict_B : {'d': 1, 'cd': 1, 'bcd': 0}
--------------------
찾았다! A:  a,  B : bcd
계산한다! A:  1 * B : 0 =  0
찾았다! A:  ab,  B : cd
계산한다! A:  1 * B : 1 =  1
1

"""