def select_candidate(test_cases: list[list[list[int]]]) -> list[int]:
    """
    다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발
    => 

    Args:
        test_cases (list[list[list[int]]]): 테스트케이스별 각 지원자의 서류 심사 순위와 면접순위가 포함된 리스트

    Returns:
        list[int]: 각 테스트케이스 별 선발할 수 있는 최대 인원수
    """
    candidates = []
    for test_case in test_cases:
        candidate = 1
        document_rank = sorted(test_case, key=lambda x: x[0])
        interview_score = document_rank[0][1]
        for num in range(1, len(test_case)):
            if interview_score > document_rank[num][1]:
                candidate += 1
                interview_score = document_rank[num][1]
        candidates.append(candidate)
    return candidates


if __name__ == "__main__":
    result = select_candidate(
        [
            [[3, 2], [1, 4], [4, 1], [2, 3], [5, 5]],
            [[3, 6], [7, 3], [4, 2], [1, 4], [5, 7], [2, 5], [6, 1]],
        ]
    )
    print(result, result == [4, 3])
