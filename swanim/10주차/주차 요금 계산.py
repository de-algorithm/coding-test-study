import math
def solution(fees, records):
    answer = []
    dic = {}
    
    for i in records:
        convert = i.split()
        convert[0] = int(convert[0][:2]) * 60 + int(convert[0][3:]) 
        if convert[1] not in dic.keys():
            dic[convert[1]] = [convert[0]] 
        else:
            dic[convert[1]].append(convert[0])
    
    car_parking_time = [] 
    dic_sorted = sorted(dic.items()) 
    for i in dic_sorted:
        if len(i[1]) % 2 != 0: 
            i[1].append(1439)
        tmp = 0
        for j in range(0, len(i[1])-1, 2):
            tmp += i[1][j+1] - i[1][j]
        
        car_parking_time.append(tmp) 
    
    print(car_parking_time)
    

    for i in car_parking_time:
        ans = fees[1] + math.ceil((i - fees[0]) / fees[2]) * fees[3]
        if i <= fees[0]: 
            answer.append(fees[1])
            continue
        answer.append(ans)
    
    return answer