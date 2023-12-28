from itertools import product


def get_plus_users(prices, users):
    revenue = [0, 0]
    for discount_rate, max_cost in users:
        filter_prices = [price[1] for price in prices if price[0] >= discount_rate]
        if sum(filter_prices) >= max_cost:
            revenue[0] += 1
        else:
            revenue[1] += sum(filter_prices)
    return revenue


def emoticon_plus_unlimited(users: list[list[int]], emoticons: list[int]) -> list[int]:
    # 각각 이모티콘의 최적 할인율을 찾아야 함 -> 어떻게??
    # 각 유저마다 할인율을 적용한 합을 구해 기준 가격과 비교 후 카운트
    candidate = []
    discount = (10, 20, 30, 40)
    discount_cases = product(discount, repeat=len(emoticons))
    for discount_case in discount_cases:
        prices = list(map(lambda x, y: (x, y*(1-x/100)), discount_case, emoticons))
        result = get_plus_users(prices, users)
        candidate.append(result)
    return sorted(candidate).pop()


if __name__ == "__main__":
    result = emoticon_plus_unlimited([[40, 10000], [25, 10000]], [7000, 9000])
    print(result, result == [1, 5400])
    result = emoticon_plus_unlimited([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])
    print(result, result == [4, 13860])