def skill_tree(skill, skill_trees):
    """
    skill: str, 1 <= len <= 26; 알파벳 대문자
    skill_trees: [str], 1 <= len <= 20;
    Skill tress의 각 엘리먼트에 skill 의 알파벳이 순서대로 들어가 되,
    바로 이어질 필요는 x, 모든 알파벳이 들어가지 않아도 되지만 이전 알파벳은 들어가야할 것
    -> return int (# of avail. skill_trees)

    - 필수 스킬트리를 dict 형태로 만듬
        키는 각 char, value는 인덱스
    - skill_trees 루프롤 통해
        - 각 skill elem들을 char list화
        - 각 elem들을 map으로 인덱스화 (C -> 0, B -> 1, D -> 2)
        - 인덱스화된 skill tree가 연속적인 숫자인지 체크
            - if true, answer += 1
    연속적인 숫자인 경우 만 갯수를 세서 리턴
    time complexity: n^2
    """

    def is_consecutive(lst):
        return lst == list(range(len(lst)))

    answer = 0
    skill_dict = dict()
    for i, skill_ch in enumerate(skill):
        skill_dict[skill_ch] = skill_dict.get(skill_ch, i)

    for each_skill in skill_trees:
        skill_lst = list(map(lambda word: skill_dict[word] if word in skill_dict else "", list(each_skill)))
        skill_lst_nonempty = list(filter(lambda each: each != "", skill_lst))
        if is_consecutive(skill_lst_nonempty):
            answer += 1
        
    return answer
