from itertools import combinations


def hold_items(n: int, c: int, weights: list[int]) -> int:
    """
    물건의 무게 목록과 최대 무게가 주어졌울 때, 최대 무게 한도 안에서 물건을 고를 때 선택의 방법의 수를 계산한다.
    Meet in the Middle 알고리즘을 이용해, 리스트를 둘로 나누어 부분합을 계산한 후 (정렬), 이분탐색을 진행한다.
    (왜 이게 투포인터 문제죠???)
    부분합은 itertools내 combination을 사용해서 부분 리스트를 구하고, list sum을 통해 합을 구한다.
    그 후, 1차적으로 정렬을 하고, 오른쪽 리스트로 for loop을 돌리며,
    각 값에 대해 왼쪽 리스트를 이분탐색으로 방법 수를 구한다.

    Args:
        n (int): 가지고 있는 물건의 갯수
        c (int): 최대로 들 수 있는 무게
        weights (list[int]): 각 물건의 무게

    Returns:
        int: n개의 물건을 가방에 넣는 방법의 수
    """
    def weight_sum(lst: list[int]) -> set[int]:
        possible_val = {0, sum(lst)} # set으로 중복 거르기. 리스트가 0보다 크다고 가정할 때 최소한 0과 리스트 전체합을 포함.
        for val in range(1, len(lst)):
            subset = list(combinations(lst, val))
            possible_val.add(sum(subset))
        return possible_val

    def meet_in_the_middle(left: list[int], right: list[int]) -> int:
        methods = 0
        left_sum = sorted(weight_sum(left)) # 0, 1, 2, 3; [1,2]의 부분합
        right_sum = sorted(weight_sum(right)) # 0, 3, 4, 7, [3,4]의 부분합
        for sum_val in right_sum:
            if sum_val > c: # 합이 이미 조건보다 크면 pass
                continue
            i, j = 0, len(left_sum) # left sum list 기준 이분탐색
            while i < j:
                m = (i+j)//2
                # m=2; 2 (index 2) + 3 <= 4라고 가정, False -> j = 2
                # m=1; 1 (index 1) + 3 <= 4라고 가정, True -> i = 2
                # while loop end (i==j)
                if left_sum[m] + sum_val <= c:
                    i = m + 1
                else:
                    j = m
            # method += 2 ; 인덱스 값 = 물건의 갯수; 총 2가지 무게를 넣을 수 있다는 의미
            # sum_val = 0이면 (오른쪽 리스트), 왼쪽 리스트에서 물건의 갯수를 고른다.
            # sum_val = 3이면 최대값 c에서 3을 제외한 나머지 무게로 왼쪽 리스트에서 물건의 갯수를 고른다.
            # 등등...
            methods += j
        return methods
    return meet_in_the_middle(weights[0:n//2], weights[n//2:n])
