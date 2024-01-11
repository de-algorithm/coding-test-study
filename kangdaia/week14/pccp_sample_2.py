from itertools import groupby


def solution(land: list[list[int]]) -> int:
    """
    각 row 별 연속적인 칸의 갯수와 col 기록
    transform
    각 row 별 연속적인 칸 합함
    ** 시간초과 오류

    Args:
        land (list[list[int]]): 1이 석유가 있는 공간, 0이 일반 땅인 2차원 공간 배열

    Returns:
        int: 석유 공간에 col을 선택했을 때, 최대로 뽑을 수 있는 석유량
    """
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    oil_cluster_ids = [[-1] * m for _ in range(n)]
    cluster_id = 0
    cluster_sizes = []

    def get_compound(m_row, m_col, cluster_id):
        if visited[m_row][m_col] or land[m_row][m_col] == 0:
            return 0

        visited[m_row][m_col] = True
        oil_cluster_ids[m_row][m_col] = cluster_id
        size = 1

        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            move_row, move_col = m_row + dx, m_col + dy
            if (
                0 <= move_row < n
                and 0 <= move_col < m
                and not visited[move_row][move_col]
                and land[move_row][move_col] == 1
            ):
                size += get_compound(move_row, move_col, cluster_id)
        return size

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                cluster_size = get_compound(i, j, cluster_id)
                cluster_sizes.append(cluster_size)
                cluster_id += 1

    max_oil = 0
    for j in range(m):
        oil_in_column = 0
        cluster_extracted = set()
        for i in range(n):
            if land[i][j] == 1:
                cluster_id = oil_cluster_ids[i][j]
                if cluster_id not in cluster_extracted:
                    oil_in_column += cluster_sizes[cluster_id]
                    cluster_extracted.add(cluster_id)
        max_oil = max(max_oil, oil_in_column)

    return max_oil
