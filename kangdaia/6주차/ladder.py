def competition(k: int, n: int, arrive: str, ladder: list[str]) -> str:
    """
    Time: O(n^2)
    1. ???가 있는 줄까지
        - 위에서 그리고 아래에서 배열 이동으로 사다리 타기
        - 각 시작점의 사람 목록과 끝점의 사람목록을 구성한 후
        - 각 라인의 기호를 읽어 배열 변경
            "*"은 그대로
            "-"은 다음 알파벳과 바꿈
    2. 물음표 줄까지 위아래로 적용후,
        - 위에서 시작해 적용한 배열과 아래서부터 시작해 적용한 배열을 비교함
        - 같은 기호는 "*"
        - 다른 기호일 경우, 다음 기호와 뒤바꿔져 있으면 "-"
        - 이외의 경우 다른 기호인데 직전 기호가 "-"이면 "*"
        - 그 외는 "x"를 리턴함
    Args:
        k (int): 총 참가한 인원 수. 사다리는 k-1개의 줄을 가진다.
        n (int): 사다리의 전체 가로줄 수
        arrive (str): 사다리를 다 탄 후 도착 순서를 나타낸 참가자 목록
        ladder (list[str]): 사다리를 기호로 나타낸 목록, 한줄은 물음표로 사다리 구성을 알 수 없다.

    Returns:
        str: 물음표 부분의 기호 목록
    """
    emtpy_row_idx = ladder.index("?"*(k-1))
    people_start = sorted(list(arrive))
    people_end = list(arrive)
    
    for s in range(emtpy_row_idx):
        curr_line = list(ladder[s]) + [""]
        for i, each_ch in enumerate(curr_line):
            if each_ch == "-":
                temp = people_start[i]
                people_start[i] = people_start[i+1]
                people_start[i+1] = temp
    
    for e in range(n-1, emtpy_row_idx-1, -1):
        curr_line = list(ladder[e])
        for j, each_ch in enumerate(curr_line):
            if each_ch == "-":
                temp = people_end[j]
                people_end[j] = people_end[j+1]
                people_end[j+1] = temp
    
    result = ""
    for l in range(k-1):
        if people_start[l] == people_end[l]:
            result += "*"
        elif people_start[l] == people_end[l+1] and people_end[l] == people_start[l+1]:
            result += "-"
        else:
            if len(result) > 0 and result[-1] == "-":
                result += "*"
            else:
                return "x"*(k-1)

    return result
