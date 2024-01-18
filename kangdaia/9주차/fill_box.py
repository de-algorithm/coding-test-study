def min_cube(box: list[int], cubes: list[int]) -> int:
    """큐브 자르기
    - 큐브 갯수 목록을 copy - 중복 pointer 방지
    - divide_box함수로 recusivly 박스를 자른다.
    - 남은 큐브 갯수와 원래 큐브 갯수 목록을 비교해, 박스를 충분히 채우는지 체크 - 부피계산 == 0
    - 부피가 0이 되지 않으면 -1, 되면, 사용한 큐브 갯수만 반환

    Args:
        box (list[int]): [length, width, height]으로 구성된 박스
        cubes (list[int]): (2**인덱스)가 큐브 사이즈인 큐브의 갯수 목록

    Returns:
        int: 박스를 채우기 위해 최소로 사용하는 큐브의 수
    """
    rest_cubes = cubes.copy()
    
    def divide_box(cut_box: list[int], i: int) -> None:
        """
        1. 남은 큐브가 없으면 끝, 인덱스가 0보다 내려가도 (남은 큐브 x) 끝, 박스 사이즈 중 0이 존재하면 (박스 부피 0) 끝
        2. 2**i로 큐브 한 변 길이를 계산하고, 박스 사이즈를 정렬한다. (가장 큰 변 길이, 가장 작은 변 길이 중요)
        3. 박스가 정육면체이고, 큐브 길이와 동일하면, 해당 큐브가 남았는지 확인 후,
            - 해당 큐브 갯수 - 1, 멈춤
        4. 위 경우에 해당하지 않으면,
            - 박스의 가장 작은 변 길이가 현재 큐브 길이보다 작거나, 현재 인덱스의 큐브 갯수가 0이면
                - 인덱스를 줄임; i - 1
                - 박스 자르기 재귀 호출
            - 박스의 가장 긴 변의 길이가 현재 큐브 길이보다 크면, 큐브 길이 간격으로 박스를 자름
            ex) 4*4*8, cube_size = 4 -> 4*4*4, 4*4*4
                - 자른 박스들을 박스 자르기 재귀 호출

        Args:
            cut_box (list[int]): 자른 박스 3-dim
            i (int): 자른박스와 비교할 큐브의 인덱스
        """
        if sum(rest_cubes) == 0 or 0 in cut_box or i < 0:  # 남은 큐브 없음
            return
        max_cube_side = 2**i
        sorted_box = sorted(cut_box)
        if all(x == max_cube_side for x in sorted_box) and rest_cubes[i] > 0:
            # 모든 변의 길이가 현재 변의 길이와 동일하고, 해당 큐브가 남아있으면, 해당 변 길이의 큐브 갯수를 -1
            rest_cubes[i] -= 1
            return
        if sorted_box[0] < max_cube_side or rest_cubes[i] == 0: 
            # 가장 작은 변의 길이가 현재 변길이보다 작거나, 현재 큐브 남은 갯수가 0이면 인덱스 -1
            divide_box(sorted_box, i-1)
        elif sorted_box[2] > max_cube_side:
            # 가장 긴 변의 길이가 현재 변의 길이보다 크면, 현재 변의 길이가 한쪽 변 길이가 되도록 분할
            divider = sorted_box[2]//max_cube_side
            cut_side = [max_cube_side for _ in range(divider)] + [sorted_box[2] % max_cube_side]
            for each_side in cut_side:
                # 자른 각 변마다 recursive
                divide_box(sorted_box[:2]+[each_side], i)
        return

    divide_box(box, len(cubes)-1)
    sum_area = 0
    for i in range(len(cubes)):
        curr_size = 2**i
        used_cube = cubes[i] - rest_cubes[i]
        sum_area += (curr_size*curr_size*curr_size)*used_cube
    box_area = box[0] * box[1] * box[2]
    if box_area - sum_area != 0:
        return -1
    return sum(cubes) - sum(rest_cubes)


def input_interpreter(input):
    box = input[0]
    cubes = input[2:]
    box_int = list(map(lambda x: int(x), box.split()))
    cubes_lst = list(map(lambda x: int(x.split()[1]), cubes))
    return box_int, cubes_lst


if __name__ == "__main__":
    test_input_1 = ["4 4 8", "3", "0 10", "1 10", "2 1"]
    box_1, cubes_1 = input_interpreter(test_input_1)
    answer = min_cube(box_1, cubes_1)
    print(answer, answer == 9)

    test_input_2 = ["4 4 8", "3", "0 10", "1 10", "2 10"]
    box_2, cubes_2 = input_interpreter(test_input_2)
    answer = min_cube(box_2, cubes_2)
    print(answer, answer == 2)

    test_input_3 = ["10 10 11", "1", "0 2000"]
    box_3, cubes_3 = input_interpreter(test_input_3)
    answer = min_cube(box_3, cubes_3)
    print(answer, answer == 1100)

    test_input_4 = ["10 10 11", "1", "0 1099"]
    box_4, cubes_4 = input_interpreter(test_input_4)
    answer = min_cube(box_4, cubes_4)
    print(answer, answer == -1)

    test_input_5 = ["37 42 59", "6", "0 143821", "1 14382", "2 1438", "3 143", "4 14", "5 1"]
    box_5, cubes_5 = input_interpreter(test_input_5)
    answer = min_cube(box_5, cubes_5)
    print(answer, answer == 5061)

    test_input_6 = ["4 4 8", "1", "0 128"]
    box_6, cubes_6 = input_interpreter(test_input_6)
    answer = min_cube(box_6, cubes_6)
    print(answer, answer == 128)
