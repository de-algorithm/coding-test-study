def solution(n):
    answer = []
    
    def hanoi(n, start, to, via):
        if n == 1:                      # 종료: 1개라면 
            answer.append([start, to])  # 출발 기둥에서 목표기둥으로 옮긴다.
            return
        else:
            hanoi(n-1, start, via, to)  # n-1개의 원판을 중간기둥으로 옮긴다. 
            answer.append([start, to])  # n번째 원판을 목적기둥으로 옮긴다. 
            hanoi(n-1, via, to, start)  # 중간기둥에 있는 n-1개의 원판을 목적기둥으로 옮긴다. 
        
    hanoi(n, 1, 3, 2)
    return answer