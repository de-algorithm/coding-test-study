from itertools import chain


def cut_paper(paper: list[list[str]]) -> list[int]:
    """
    # recursive program
    # inside recursive func, divide_row
    1. row, col 길이 체크 (무조건 row >= col)
    2. row 길이가 3보다 작으면 (더이상 나눌 수 없음)
        - 안에 있는 값을 찾아서, count의 해당 인덱스 값을 +1
        - ex) 안에 값이 0이면, count[0] + 1, 안에 값이 -1이면, count[-1] + 1
        - return count
    3. row 길이가 아직 3이상이면, (3등분 가능)
        - 3등분 할 간격을 구해서
        - for loop으로 간격만큼 paper row를 나눔
        - 나눠진 paper rows를 transpose 
            -> [3,3] 크기를 3등분 해서 [1,3]으로 만든 후 [3,1]로 만드는 것
        - transposed 된 paper를 recursive로 호출
            - recursive로 나온 count값으로 다음 recursive 호출
        return count
    4. count 값 순서가 원하는 값 순서와 달라서, 마지막 -1 인덱스를 0번 인덱스로 이동

    Args:
        paper (list[list[str]]): 2D-list representing paper, each cell can be -1, 0, or 1

    Returns:
        list[int]: count identical paper and update value (-1/0/1) in corresponding index
    """
    def divide_row(space: list[list[str]], count: list[int]) -> list[int]:
        n, m = len(space), len(space[0])
        if n < 3:
            val = int(space[0][0])
            count[val] += 1
            return count
        margin = n // 3
        if n == m:
            flatten = list(chain.from_iterable(space))
            last = flatten.pop()
            if all(last == x for x in flatten):
                count[int(last)] += 1
                return count
        mod_count = count
        for i in range(0, n, margin):
            row_div = space[i:i+margin]
            col_trans = list(zip(*row_div))
            mod_count = divide_row(col_trans, mod_count)
        return mod_count
    result = divide_row(paper, [0, 0, 0])
    return [result.pop()]+result


if __name__ == "__main__":
    test_input1_board = [
        "0 0 0 1 1 1 -1 -1 -1",
        "0 0 0 1 1 1 -1 -1 -1",
        "0 0 0 1 1 1 -1 -1 -1",
        "1 1 1 0 0 0 0 0 0",
        "1 1 1 0 0 0 0 0 0",
        "1 1 1 0 0 0 0 0 0",
        "0 1 -1 0 1 -1 0 1 -1",
        "0 -1 1 0 1 -1 0 1 -1",
        "0 1 -1 1 0 -1 0 1 -1"
    ]
    test_input1_board = list(map(lambda x: x.split(), test_input1_board))
    print("PASS" if cut_paper(test_input1_board) == [10, 12, 11] else "FAIL")
    test_input2_board = [
        "0 1 0",
        "1 0 0",
        "0 -1 0"
    ]
    test_input2_board = list(map(lambda x: x.split(), test_input2_board))
    print("PASS" if cut_paper(test_input2_board) == [1, 6, 2] else "FAIL")
    test_input3_board = [
        "0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0"
    ]
    test_input3_board = list(map(lambda x: x.split(), test_input3_board))
    print("PASS" if cut_paper(test_input3_board) == [0, 1, 0] else "FAIL")
    test_input4_board = [
        "1 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 -1"
    ]
    test_input4_board = list(map(lambda x: x.split(), test_input4_board))
    print("PASS" if cut_paper(test_input4_board) == [1, 23, 1] else "FAIL")
