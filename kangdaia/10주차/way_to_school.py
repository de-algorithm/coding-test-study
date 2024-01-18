def find_path(n: int, m: int, puddles: list[list[int]]) -> int:
    """
    
    
    Args:
        n (int): rows number
        m (int): cols number
        puddles (list[list[int]]): locations of ponds

    Returns:
        int: methods of 
    """
    dp = [[1 for _ in range(m)] for _ in range(n)]
    for puddle in puddles:
        if puddle[0]-1 == 0:
            for i in range(puddle[1], n):
                dp[i][puddle[0]-1] = 0
        if puddle[1]-1 == 0:
            for i in range(puddle[0]-1, m):
                dp[puddle[1]-1][i] = 0
        dp[puddle[1]-1][puddle[0]-1] = 0
    for x in range(m):
        # 각 단계별 선택지: 오른쪽, 아래
        for y in range(n):
            if dp[y][x] != 0 and x>0 and y>0:
                dp[y][x] = (dp[y-1][x] + dp[y][x-1]) % 1_000_000_007
    return dp[-1][-1]
