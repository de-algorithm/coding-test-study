def surveillance_camera(routes):
    routes.sort(key=lambda x: (x[1], x[0]))
    i = 1
    m = 30_000
    for s, e in routes:
        if s > m:
            i += 1
            m = e
        m = min(e, m)
    return i
