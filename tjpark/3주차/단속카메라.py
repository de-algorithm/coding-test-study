# 11:30
# 모든 차량이 한번은 단속 카메라를 만나도록 하는 최소 카메라 갯수
# [진입, 진출] 리스트가 주어짐
# 진입 기준으로 정렬 후 겹치는지 확인
# 진출 다음 진입 보다 작으면 카메라 수 +1

def solution(routes):
    answer = 1
    routes.sort(key =lambda x :x[1])
    cam_check = routes[0][1]
    for in_, out_ in routes:
        
        if cam_check < in_:
            answer += 1
            cam_check = out_
        
    return answer