from heapq import heappop, heappush


def executor(n: int, m: int, x: int, y: int, r: int, c: int, k: int) -> str:

    def difference(i, j):
        return abs(r - i) + abs(c - j)
    distance = [("", difference(x, y), x, y)]

    while distance:
        prev, _, curr_r, curr_c = heappop(distance)
        if r == curr_r and c == curr_c:
            if len(prev) == k:
                return prev
            if (k - len(prev)) % 2:
                break
        # down
        if 1 <= curr_r + 1 <= n:
            estimate = len(prev) + 1 + difference(curr_r+1, curr_c)
            if estimate <= k:
                heappush(distance, (prev+"d", estimate, curr_r+1, curr_c))
        # up
        if 1 <= curr_r - 1 <= n:
            estimate = len(prev) + 1 + difference(curr_r-1, curr_c)
            if estimate <= k:
                heappush(distance, (prev+"u", estimate, curr_r-1, curr_c))
        # left
        if 1 <= curr_c - 1 <= m:
            estimate = len(prev) + 1 + difference(curr_r, curr_c-1)
            if estimate <= k:
                heappush(distance, (prev+"l", estimate, curr_r, curr_c-1))
        # right
        if 1 <= curr_c + 1 <= m:
            estimate = len(prev) + 1 + difference(curr_r, curr_c+1)
            if estimate <= k:
                heappush(distance, (prev+"r", estimate, curr_r, curr_c+1))
    return "impossible"

