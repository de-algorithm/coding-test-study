from itertools import product
from heapq import heappop, heappush


def waiting_time(mentor_dist, reqs):
    slots = []
    total_waiting = 0
    for n in mentor_dist:
        slots.append([0 for _ in range(n)])
    for req in reqs:
        start_t, req_t, req_type = req
        prev_end_t = heappop(slots[req_type-1])
        total_waiting += max(0, prev_end_t-start_t)
        heappush(slots[req_type-1], max(start_t, prev_end_t)+req_t)
    return total_waiting


def recruiting(k: int, n: int, reqs: list[list[int]]) -> int:
    mentors_prods = product(range(1, n+1), repeat=k)
    min_waiting = float("inf")
    for mentors_prod in mentors_prods:
        if sum(mentors_prod) == n:
            total_wait = waiting_time(mentors_prod, reqs)
            min_waiting = min(min_waiting, total_wait)
    return min_waiting


if __name__ == "__main__":
    result = recruiting(3, 5, [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]])
    print(result, result == 25)
    result = recruiting(2, 3, [[0,100,1],[5,100,2],[10,100,1],[15,30,2],[20,100,1],[45,10,2],[60,5,2]])
    print(result, result == 270)
    result = recruiting(2, 3, [[0,100,1],[5,100,2],[10,100,1],[15,30,2],[20,100,1],[45,10,2],[60,5,2]])
    print(result, result == 270)
