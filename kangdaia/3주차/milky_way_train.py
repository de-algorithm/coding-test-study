def travel_milky_way(n:int, orders: list[str]) -> int:
    """
    주어진 명령에 따라 위치 변경 후 중복되지 않는 리스트 갯수 세기
    1&2 -> 1은 해당 위치에 1 부여, 2는 0 부여
    3 -> 리스트 한칸씩 오른쪽으로 밀기
    4 -> 리스트 한칸씩 왼쪽으로 밀기

    Args:
        n (int): 기차의 수 (1 ≤ N ≤ 100000)
        orders (list[str]): 숫자 2개 혹은 3개로 구성된 명령의 목록

    Returns:
        int: 은하수를 건널 수 있는 기차의 수 (중복되지 않는 목록 수)
    """
    SEAT_LENGTH = 20
    #  []*20 : each element in the list is pointing to the SAME list object
    train = [[0 for _ in range(SEAT_LENGTH)] for _ in range(n)]

    for order in orders:
        order_lst = order.split()
        ty_order, train_num = order_lst[0], int(order_lst[1])-1
        if ty_order == "1" or ty_order == "2":
            seat_num = int(order_lst[2])-1
            train[train_num][seat_num] = 1 if ty_order == "1" else 0
        elif ty_order == "3":
            train[train_num] = [0] + train[train_num][:SEAT_LENGTH-1]
        elif ty_order == "4":
            train[train_num] = train[train_num][1:SEAT_LENGTH] + [0]

    return len(set(tuple(x) for x in train))