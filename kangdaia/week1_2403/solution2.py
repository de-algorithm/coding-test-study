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


def solution(k, n, reqs):
    mentors_prods = product(range(1, n+1), repeat=k)
    min_waiting = float("inf")
    for mentors_prod in mentors_prods:
        if sum(mentors_prod) == n:
            total_wait = waiting_time(mentors_prod, reqs)
            min_waiting = min(min_waiting, total_wait)
    return min_waiting