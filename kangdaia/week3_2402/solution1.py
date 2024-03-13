import re


def solution(timelogs: list[str]) -> int:
    price = 0
    for timelog in timelogs:
        h, m, d = re.split("[:\s]", timelog)
        h, m, d = int(h), int(m), int(d)
        if h >= 7 and h < 19:
            remain = 0
            if m + d > 60 and int(h) == 18:
                remain = m + d - 60
            price += (d - remain) * 10 + remain * 5
        else:
            remain = 0
            if m + d > 60 and int(h) == 6:
                remain = m + d - 60
            price += (d - remain) * 5 + remain * 10
    return price
