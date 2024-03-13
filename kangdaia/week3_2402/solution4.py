def solution(n, s):
    middle_val = s // n
    repeat_val = s % n
    if n > s:
        return [-1]

    return [middle_val] * (n - repeat_val) + [middle_val + 1] * repeat_val
