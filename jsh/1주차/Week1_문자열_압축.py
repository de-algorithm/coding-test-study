# Lv.2
# 시작시간 : 11:20
# 끝난시간 : 12:04
"""
1. 문자열을 몇 개 단위로 자를지 : num_slice
2. 처음나온( 앞으로 다른것들과 비교할 ) 문자열 넣어놓을 변수 : check_word
3. 비교할 문자열 넣어놓을 변수 : now
4. 같은 문자열이 몇 번 반복되었는지 넣어놓을 변수 : count
5. 현재 검사중인 위치 : current_index
***
1. 문자열의 절반길이만큼 반복문을 돌린다 ( for num_slice ...)
2. 검사할 처음나온 문자열(check)을 선언 후 그 이후에 나올 문자열과 검사한다 
2-0. 현재 검사중인 문자열 위치 ( current_index )
2-1. 다음에 나온 문자열이 같으면 count += 1
2-2. 다음에 나온 문자열이 같지 않으면  check 를 다음 문자열로 바꾼다

"""
def solution(s):
    answer = len(s)
    for num_slice in range(1,int(len(s)/2)+1):
        result = ''
        count = 1
        check_word = s[0:num_slice]
        for current_index in range(num_slice,len(s),num_slice):
            now = s[current_index:current_index+num_slice]
            if check_word == now :
                count += 1
            else :
                if count != 1:
                    result += str(count)
                result += check_word
                count = 1
            check_word = now
        if count != 1:
            result += str(count)
        result += check_word
        answer = min( answer, len(result))
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.32ms, 10MB)
# 테스트 3 〉	통과 (0.22ms, 10.3MB)
# 테스트 4 〉	통과 (0.03ms, 10.1MB)
# 테스트 5 〉	통과 (0.00ms, 10MB)
# 테스트 6 〉	통과 (0.03ms, 10.3MB)
# 테스트 7 〉	통과 (0.57ms, 9.95MB)
# 테스트 8 〉	통과 (0.52ms, 10.3MB)
# 테스트 9 〉	통과 (0.47ms, 10.3MB)
# 테스트 10 〉	통과 (2.01ms, 10.1MB)
# 테스트 11 〉	통과 (0.07ms, 10.1MB)
# 테스트 12 〉	통과 (0.07ms, 10.3MB)
# 테스트 13 〉	통과 (0.09ms, 10.2MB)
# 테스트 14 〉	통과 (0.48ms, 10.2MB)
# 테스트 15 〉	통과 (0.11ms, 10.1MB)
# 테스트 16 〉	통과 (0.02ms, 10.3MB)
# 테스트 17 〉	통과 (0.86ms, 10.2MB)
# 테스트 18 〉	통과 (0.81ms, 10.1MB)
# 테스트 19 〉	통과 (1.51ms, 10.2MB)
# 테스트 20 〉	통과 (2.07ms, 10.1MB)
# 테스트 21 〉	통과 (1.91ms, 10.1MB)
# 테스트 22 〉	통과 (1.91ms, 10.2MB)
# 테스트 23 〉	통과 (1.83ms, 10.1MB)
# 테스트 24 〉	통과 (1.73ms, 10.2MB)
# 테스트 25 〉	통과 (1.99ms, 10.3MB)
# 테스트 26 〉	통과 (1.88ms, 10.1MB)
# 테스트 27 〉	통과 (1.93ms, 10.1MB)
# 테스트 28 〉	통과 (0.02ms, 10.3MB)
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

## 저 if count != 1:.. 를 어떻게 예쁘게 고치고싶다