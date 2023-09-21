# 자를 수 있는 경우를 모두 구하고 비교하기
# 첫번째 문자 포함해서 반복이 되어야 함
# 문자열의 길이 중간+1까지 반복되는 문자 없으면 압축 불가
def solution(s):
    answer = len(s)

    for i in range(1, len(s)//2 + 1):
        # 문자가 반복하면 어떤 문자열인지 저장, 몇 번 반복하는지 확인
        count = 1
        std_str = s[:i]
        result_str = ""
        
        for j in range(i, len(s), i):
            # 반복 o / count +1
            if std_str == s[j:j+i]:
                count += 1
            # 반복 x / 전에 카운트된 숫자와 문자열 저장 
            else:
                if count > 1:
                    result_str += str(count)
                result_str += std_str
                std_str = s[j:j+i]
                count = 1
        
        # 압축 후 나머지 문자열 저장
        if count > 1:
            result_str += str(count)
        result_str += std_str
        
        # 문자열 길이 최소값 구하기
        if answer > len(result_str):
            answer = len(result_str)
            
    return answer
