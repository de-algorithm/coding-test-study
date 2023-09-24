def solution(skill, skill_trees):
    answer = 0
    
    for i in range(len(skill_trees)): # 스킬트리 전체 순회
        flag = 0
        pointer = 0
        for j in range(len(skill_trees[i])): # 스킬트리 원소 값 순회
            if skill_trees[i][j] in skill: # 스킬 트리 원소가 skill안에 있다면
                if skill_trees[i][j] == skill[pointer]: # 스킬트리 원소와 현재 skill 원소값이 동일하면
                    if pointer != len(skill)-1:
                        pointer += 1
                    else:
                        break
                else:
                    flag = 1
        if flag == 0 : 
            answer += 1
    return answer