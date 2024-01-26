def build_frame_solution(n, build_frame):
    return solution_brute_force(n, build_frame)


def build_cond(curr):
    def check_cond(elem):
        x, y, a = elem
        if a == 0:  # 기둥
            return y == 0 or [x, y-1, 0] in curr or [x-1, y, 1] in curr or [x, y, 1] in curr
        else:  # 보
            return [x, y-1, 0] in curr or [x+1, y-1, 0] in curr or ([x+1, y, 1] in curr and [x-1, y, 1] in curr)
    
    return all(map(lambda elem: check_cond(elem), curr)) 


def solution_brute_force(n, build_frame):
    answer = []
    while build_frame:
        x, y, a, b = build_frame.pop(0)
        if b == 0 and [x, y, a] in answer:  # 삭제
            answer.remove([x, y, a])
            if not build_cond(answer):
                answer.append([x, y, a])
        elif b == 1 and [x, y, a] not in answer:  # 추가
            answer.append([x, y, a])
            if not build_cond(answer):
                answer.remove([x, y, a])

    answer.sort()
    return answer
