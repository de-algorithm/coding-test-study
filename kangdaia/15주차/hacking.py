from collections import defaultdict
from heapq import heappop, heappush


def find_hacked_computer(N: int, D: int, c: int, deps: list[str]) -> tuple[int, int]:
    """의존성으로 연결되어 시작 컴퓨터부터 연결된 모든 컴퓨터(노드)의 갯수와 마지막 컴퓨터를 찾기까지 시간
    1. 그래프 초기화: "a b s"형태로 되어있는 의존성 리스트를 b -> a = s 가 되도록 바꿈
        - defaultdict 사용
    2. visited도 defaultdict 사용해 float("inf")로 초기화
    3. 시작 노드와 0 (가중치)로 visited와 heap 구성
    4. heap이 빌 때까지,
        - heap에서 가장 가중치가 적은 노드의 값을 가져와,
        - 만약 이미 방문해서 더 작은 가중치 값을 가지고 있다면 pass
        - 현재 가중치 기준으로 최대값 확인 (연결된 노드를 모두 방문하기까지 시간을 구해야 하기 때문)
        - 아닐 경우, 인접 노드를 찾아서, 각 인접노드의 새로운 가중치를 구하고,
        - 새로운 가중치가 방문 목록의 값보다 작으면 갱신 
        (방문하지 않았다면 infinite, 방문했어도 더 작은값이면 갱신)
        - heap에 추가함
    5. visited 목록을 확인해, infinite 값이 아닌 노드의 수를 셈

    Args:
        N (int): 컴퓨터 개수
        D (int): 의존성 개수
        c (int): first hacked computer number (starting node)
        dep (list[str]): "a b t" 형태로, a 가 b에 의존한다는 의미
        각 컴퓨터 (노드) 간의 의존성 및 감염 시간 (가중치)을 나타냄

    Returns:
        tuple[int, int]: 감염된 컴퓨터 대수와 감염되기까지 전체 시간
    """
    graph = dict()
    for dep in deps:
        a, b, s = dep.split()
        if int(b) not in graph:
            graph[int(b)] = defaultdict(lambda: float("inf"))
        graph[int(b)][int(a)] = int(s)
    
    visited = defaultdict(lambda: float("inf"))
    visited[c] = 0
    heap = []
    heappush(heap, (0, c))
    total_time = float("-inf")

    while heap:
        t, num = heappop(heap)

        if visited[num] < t:
            continue
        total_time = max(t, total_time)

        neighbors = graph[num].items() if num in graph else []
        for next_num, next_t in neighbors:
            new_t = next_t + t
            if new_t < visited[next_num]:
                visited[next_num] = new_t
                heappush(heap, (new_t, next_num))

    count_comp = 0
    for _ , v in visited.items():
        if v < float("inf"):
            count_comp += 1
    return (count_comp, total_time)

if __name__ == "__main__":
    print("========TEST 1=========")
    testN = 2
    testcase = map(lambda x: int(x), "3 2 2".split())
    dependency = ["2 1 5", "3 2 5"]
    result_testcase = find_hacked_computer(*testcase, dependency)
    print(result_testcase, result_testcase == (2, 5))

    testcase = map(lambda x: int(x), "3 3 1".split())
    dependency = ["2 1 2", "3 1 8", "3 2 4"]
    result_testcase = find_hacked_computer(*testcase, dependency)
    print(result_testcase, result_testcase == (3, 6))