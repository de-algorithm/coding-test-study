def puzzle_solver(n: int) -> list[list[int]]:
    """하노이의 탑
    한번에 하나의 원판만 옮길 수 있고 큰 원판이 작은 원판 위에 있어서는 안될 때,
    최소의 움직임으로 n개의 원판을 1번 기둥에서 3번 기둥으로 옮기는 방법을 찾는다.
    n개의 원판을 옮기기 위해서는 n-1개의 원판을 중간 기둥까지 옮겨야 하고 (재귀),
    1번 기둥에서 3번 기둥으로 n번째 원판을 옮긴다.
    다시 중간 기둥에 위치한 n-1개의 원판을 3번 기둥으로 옮기면 (재귀),
    n개의 원판을 옮기는 데 성공한다.
    Args:
        n (int): 1번 기둥에 있는 원판의 갯수

    Returns:
        list[list[int]]: n개의 원판을 최소로 3번 원판으로 옮기는 방법
    """
    methods = []

    def recurse_move(tower_n, curr, end):
        next_pos = 6 - end - curr
        if tower_n == 1:
            methods.append([curr, end])
        else:
            recurse_move(tower_n-1, curr, next_pos)
            methods.append([curr, end])
            recurse_move(tower_n-1, next_pos, end)
    recurse_move(n, 1, 3)
    return methods
