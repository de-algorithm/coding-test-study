from heapq import heappop, heappush
from collections import defaultdict


def find_sibling(N: int, K: int) -> int:
    """
    조건:
    - 현위치 x에서 x-1 혹은 x+1로 이동가능, 이동시간은 1초 (가중치)
    - 순간이동시 0초의 시간으로 x위치에서 2*x위치로 이동 가능

    도착 위치를 찾는 조건으로 빠른 시간이 1순위

    Args:
        N (int): 출발 위치
        K (int): 도착 위치

    Returns:
        int: 출발 위치에서 도착 위치까지 가장 빠른 시간
    """
    dist = defaultdict(lambda: float("inf"))
    dist[N] = 0
    heap = []
    heappush(heap, (0, N))
    result = float("inf")

    while heap:
        t, node = heappop(heap)
        if node == K:
            result = min(result, t)

        if dist[node] < t or node < 0 or node > 100000:
            continue
        
        neighbors = [[t+1, node-1], [t+1, node+1], [t, node*2]]
        for next_t, next_node in neighbors:
            if next_t < dist[next_node] and 0 <= next_node <= 100000:
                dist[next_node] = next_t
                heappush(heap, (next_t, next_node))

    return result


if __name__ == "__main__":
    print("=========TEST 1=========")
    test = find_sibling(5, 17)
    print(test, test == 2)
    print("=========TEST 2=========")
    test = find_sibling(0, 0)
    print(test, test == 0)
    print("=========TEST 3=========")
    test = find_sibling(2, 7)
    print(test, test == 1)
    print("=========TEST 4=========")
    test = find_sibling(1, 17)
    print(test, test == 1)
    print("=========TEST 5=========")
    test = find_sibling(1, 32)
    print(test, test == 0)
    print("=========TEST 6=========")
    test = find_sibling(1, 10000)
    print(test, test == 3)
