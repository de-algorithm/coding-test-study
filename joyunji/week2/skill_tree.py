'''
Date        : 2024.01.29
Problem     : https://school.programmers.co.kr/learn/courses/30/lessons/49993
Tag         : 구현
'''


def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:            # skill trees 순회
        seq = [False]*len(skill)              # 선행 스킬 순서 확인을 위한 배열 
        for i in skill_tree:                  # 스킬 트리       
            if i in skill:                    # 스킬이 선행스킬에 포함된다면
                skill_index = skill.index(i)
                if skill_index == 0:          # 선행 스킬 순서의 첫 번째일 때
                    seq[0] = True             # 올바른 순서이므로 true 
                else:                       
                    if seq[skill_index-1]:      # 앞 순서의 스킬을 배웠다면 
                        seq[skill_index] = True # 올바른 순서로 판단
                    else:                       
                        break
        else: 
            answer += 1                         # for문을 break 없이 전부 순회했다면 가능한 스킬트리로 판단 

    return answer