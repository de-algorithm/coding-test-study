def solution(n: int, seq: list[int], ops: list[int]) -> list[int]:
    """연산자 추가하기

    Args:
        n (int): 수열의 개수 N(2 ≤ N ≤ 11)
        seq (list[int]): A_1, A_2, ..., A_N(1 ≤ A_i ≤ 100)로 구성된 수열 (정수) list
        ops (list[int]): length = 4, 4개의 정수 list - 각 숫자는 덧셈, 뺄셈, 곱셈, 나눗셈의 갯수.

    Returns:
        [int, int]: 결과의 최댓값과 최솟값을 반환, -10억보다 크거나 같고, 10억보다 작거나 같은 결과
    """
    base_elem = seq[0]
    result = []
    # 재귀함수

    def seq_ops_helper(calc, idx, ops):
        if idx == n:
            result.append(calc)  # 수열의 모든 숫자를 사용하면 결과 값 후보 list에 추가
            return 0

        if ops[0]:  # 더하기
            seq_ops_helper(
                calc + seq[idx], idx + 1, [ops[0] - 1, ops[1], ops[2], ops[3]]
            )
        if ops[1]:  # 빼기
            seq_ops_helper(
                calc - seq[idx], idx + 1, [ops[0], ops[1] - 1, ops[2], ops[3]]
            )
        if ops[2]:  # 곱하기
            seq_ops_helper(
                calc * seq[idx], idx + 1, [ops[0], ops[1], ops[2] - 1, ops[3]]
            )
        if ops[3]:  # 나누기
            # Python에서 //연산자는 몫보다 작거나 같은 정수를 선택하고, /연산자는 소수 부분을 버리기 때문입니다
            seq_ops_helper(
                int(calc / seq[idx]), idx + 1, [ops[0], ops[1], ops[2], ops[3] - 1]
            )

    seq_ops_helper(base_elem, 1, ops)
    # min 함수의 공식 Documentation을 보면, 둘 이상의 원소가 최소일 때는 그 중 가장 먼저 등장하는 원소를 반환.
    return [max(max(result), -1e9), min(min(result), 1e9)]
