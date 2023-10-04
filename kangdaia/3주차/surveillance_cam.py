def surveillance_camera(routes):
    """_summary_

    Args:
        routes (list): _description_

    Returns:
        int: _description_
    """
    routes.sort(key=lambda x: (x[1], x[0]))
    i = 1
    m = 30_000
    for s, e in routes:
        if s > m:
            i += 1
            m = e
        m = min(e, m)
    return i
