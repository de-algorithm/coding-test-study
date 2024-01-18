def cache_loadtime(cacheSize: int, cities: list[str]) -> int:
    """
    Least Recently Used 알고리즘을 적용해, 각 캐시사이즈에 맞에
    도시이름 배열을 순서대로 처리할 때, hit은 실행시간 1, miss는 실행시간 5로 측정해
    그 값을 합산해 돌려준다.
    주의점:
    - 도시목록은 대문자,소문자 상관없이 섞여있다.
    - cacheSize는 0 이상이다

    Args:
        cacheSize (int): 캐시(스택)크기
        cities (list[str]): 도시이름 배열

    Returns:
        int: 총 실행시간의 합
    """
    cacheDB = []
    total_load = 0
    for city in cities:
        city = city.capitalize()
        total_load += 1 if city in cacheDB else 5
        if cacheSize > 0:
            if city not in cacheDB:
                if len(cacheDB) == cacheSize:
                    cacheDB.pop(0)
                cacheDB.append(city)
            else:
                cacheDB.remove(city)
                cacheDB.append(city)

    return total_load
