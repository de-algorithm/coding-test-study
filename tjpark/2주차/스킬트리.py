# input: 선행 스킬 순서 문자열(skill), 스킬트리를 담은 배열(skill_trees)
# return: 스킬트리중 가능한 배울 수 있는 갯수
# 스킬 중복 x, 순서대로만 배워야함
# 선행 skill 필요없으면 배울 수 있음
def solution(skill, skill_trees):
    answer = 0
    
    for st in skill_trees:
        idx = 0
        for s in st:
            # 스킬을 배울 수 있을 때
            if s == skill[idx]:
                idx += 1
                # skill을 순서대로 모두 사용했을 경우
                if idx == len(skill):
                    answer += 1
                    break
            
            # 선행 스킬 없이 배우려고 할 때
            elif s in skill and s != skill[idx]:
                break
            
            # 모두 확인 했을 때
            if s == st[-1]:
                answer += 1
                
    return answer
