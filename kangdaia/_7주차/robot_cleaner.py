def cleaning_area(robot: list[int], room: list[list[int]]) -> int:
    """_summary_
    1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    2. 현재 칸의 주변 칸 중 청소되지 않은 빈 칸이 없는 경우,
        - 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        - 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
    3. 현재 칸의 주변 칸 중 청소되지 않은 빈 칸이 있는 경우,
        - 반시계 방향으로 90도 회전한다.
        - 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        - 1번으로 돌아간다.
    Args:
        robot (list[int]): 3 elems robot init coord (x,y) 좌표 & 방향 (0, 1, 2, 3)
        room (list[list[int]]): n*m list

    Returns:
        int: number of area cleaned
    """
    curr = robot[:2]
    direction = robot[2]
    area = 0
    n, m = len(room), len(room[0])

    while True:
        if room[curr[0]][curr[1]] == 0:
            area += 1
            room[curr[0]][curr[1]] = -1
        left = room[curr[0]][curr[1]-1] if curr[1] > 0 else 1
        right = room[curr[0]][curr[1]+1] if curr[1] < m-1 else 1
        top = room[curr[0]-1][curr[1]] if curr[0] > 0 else 1
        bottom = room[curr[0]+1][curr[1]] if curr[0] < n-1 else 1
        check_any_not_clean = any([left==0, right==0, top==0, bottom==0])
        if not check_any_not_clean:
            if [bottom, left, top, right][direction] == 1:
                break
            if direction == 0:
                curr = [curr[0]+1, curr[1]]
            elif direction == 2:
                curr = [curr[0]-1, curr[1]]
            elif direction == 1:
                curr = [curr[0], curr[1]-1]
            else:
                curr = [curr[0], curr[1]+1]
        else:
            direction = direction-1 if direction > 0 else 3
            if [top, right, bottom, left][direction] == 0:
                if direction == 0:
                    curr = [curr[0]-1, curr[1]]
                elif direction == 2:
                    curr = [curr[0]+1, curr[1]]
                elif direction == 1:
                    curr = [curr[0], curr[1]+1]
                else:
                    curr = [curr[0], curr[1]-1]
    return area