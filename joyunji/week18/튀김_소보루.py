def solution(n, s, times):  
    answer = n-s
    
    l = 0
    r = n-s
    
    while l <= r:
        m = (l + r) // 2    # m초 
        # sum : 0~m초동안 먹는(잡는) 소보루 총 개수
        ## 0초에는 모든 사람이 소보루를 잡기 때문에 사람 수로 초기화
        sum = len(times)
        # 해당 시간에 소보루를 집는 사람 번호 리스트
        li = [] 
        
        for i in range(len(times)):
            sum += m//times[i]
            if m%times[i] == 0:
                li.append(i+1)  
        
        # sum은 m초에 마지막에 잡은 소보루의 번호
        # 소보루 번호는 1~n (잡는 순서대로)
        # 소보루의 총 개수가 먹은 소보루 개수(answer)보다 작은 경우
        if sum < answer:
            l = m
        # 마지막에 잡은 소보루 번호와 먹은 소보루 개수가 같은 경우
        elif sum == answer:
            return li[-1]
        # 소보루의 총 개수가 먹은 소보루 개수보다 큰 경우
        else:
            # m초에 처음 잡은 소보루 번호가 먹은 소보루 개수보다 큰 경우
            if sum-len(li)+1 > answer:
                r = m
            # m초에 answer번째 소보루를 먹은 경우
            else:
                # 몇번 사람이 answer번째 소보루를 잡았는지 계산하기
                diff = answer-(sum-len(li)+1)
                return li[diff]


