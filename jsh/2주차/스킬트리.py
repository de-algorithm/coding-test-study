# start -> 17:30
# end -> 18:00
"""
1. 스킬트리에 대해 스킬에 해당하는 스펠링만 추출하여 하나의 배열로 만든다
-> 예제기준 " BACDE " > " B C D " 

2. 추출된 배열은 skill에 대한 순서와 동일해야 하므로 동일한지 아닌지 ( is_possibale )를 체크한다
"""
def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        order = []  # 스킬 트리에 나타난 스킬들의 순서를 저장하는 리스트
        is_possible = True  # 현재 스킬 트리가 가능한지 여부를 나타내는 변수
        
        # 1.
        for s in skill_tree:
            if s in skill:
                order.append(s)
        # print(order)
        """
        ["BACDE", "CBADF", "AECB", "BDA"] ->
        ['B', 'C', 'D']
        ['C', 'B', 'D']
        ['C', 'B']
        ['B', 'D']
        """
        
        # 2.
        for i in range(len(order)):
            if order[i] != skill[i]:
                is_possible = False
                break
        
        if is_possible:
            # print(order)
            """
            ['C', 'B', 'D']
            ['C', 'B']
            """
            answer += 1
        
    return answer