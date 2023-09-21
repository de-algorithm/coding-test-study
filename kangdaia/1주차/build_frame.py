def build_frame_solution(n, build_frame):
    return solution_brute_force(n, build_frame)

def build_cond(curr):
    ## 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
    ## 벽면을 벗어나게 기둥, 보를 설치하는 경우는 없습니다.
    ## 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
    ## 바닥에 보를 설치 하는 경우는 없습니다.
    def check_cond(x, y, a):
        if a == 0:
            return y == 0 or [x, y-1, 0] in curr or [x-1, y, 1] in curr or [x, y, 1] in curr # 기둥이 바닥에 있다
        else:
            return y != 0 or [x, y, 0] in curr or [x+1, y, 1] in curr or [x-1, y, 1] in curr
    
    return all(map(lambda x, y, a: check_cond(x,y,a), curr))


def solution_brute_force(n, build_frame):
    answer = []
    while(build_frame):
        x, y, a, b = build_frame.pop(0)
        if b==0 and [x, y, a] in answer:
            answer.remove([x, y, a])
            if not build_cond(answer):
                answer.append([x, y, a])
        elif b==1 and [x, y, a] not in answer:
            answer.append([x, y, a])
            if not build_cond(answer):
                answer.remove([x, y, a])
    
    answer.sort()
    return answer