# 첫째 줄에 문자열이 주어진다. 문자열의 길이는 1보다 크거나 같고, 1,000,000보다 작거나 같다.

# 둘째 줄에 폭발 문자열이 주어진다. 길이는 1보다 크거나 같고, 36보다 작거나 같다.

# 두 문자열은 모두 알파벳 소문자와 대문자, 숫자 0, 1, ..., 9로만 이루어져 있다.




import sys


def solution():
    S = sys.stdin.readline().rstrip()
    check_word = sys.stdin.readline().rstrip()

    len_check = len(check_word)
    answer = []
    
    
    for w in S :
        answer.append(w)
        # print(f'check : {answer[-len_check:]} ')
        if ''.join(answer[-len_check:]) == check_word :
            for _ in range(len_check):
                answer.pop()
                # print(f'pop!! {answer}')
        
        # print(answer)        
    
    if answer :
        print(''.join(answer))
    else :
        print('FRULA')
        
    
    


if __name__ == '__main__':
    solution()
    