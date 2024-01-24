import sys

sys.stdin = open('yunji/input.txt', 'r')
input = sys.stdin.readline

string = input().rstrip('\n')
explosion = input().rstrip('\n')



# 시간 초과 풀이
# while explosion in string:
#         string = string.replace(explosion, "")


# 슬라이딩 윈도우 풀이 -> 인덱스 조절이 어려움, for문 횟수 조절이 유동적으로 안됨
# str_len = len(string)
# ep_len = len(explosion)

# for i in range(len(string)):
#     print(i)
#     if string[i:i+4] == explosion:
#         print("포함")
#         string = string[:i] + string[i+4:]
#     print(string)

# 스택 풀이
st = []



if string:
    print(string)
else:
    print("FRULA")


