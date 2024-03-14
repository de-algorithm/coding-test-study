def ps_card_collector(purchase: int, price: str) -> int:
    """
    구매할 카드 개수에 맞춰 카드팩을 구매할 때 가장 비싼 가격을 알려준다.
    가격 정보 목록은 리스트의 인덱스가 카드팩에 들어가 있는 카드 갯수이다.
    (중복허용)
    Args:
        purchase (int): 구매할 카드 개수
        price (str): 스페이스로 구분된 각 카드팩의 가격 정보 목록

    Returns:
        int: 카드를 가지기위해 지불해야하는 금액의 최댓값
    """
    """
    # 재귀 그리디 방식 time: O(n^n)
    price_list = price.split()
    result = set()

    def recurse_ps_card(left_card, price):
        if left_card < 0:
            return -1
        elif left_card == 0:
            result.add(price)
            return price
        for i, each_price in enumerate(price_list):
            recurse_ps_card(left_card-(i+1), int(each_price)+price)

    for i, each_price in enumerate(price_list):
        recurse_ps_card(purchase-(i+1), int(each_price))

    return max(result)
    """
    # dp 방식 time: n^2
    price_list = price.split()
    dp = [int(x) for x in price_list]
    for i in range(1, len(price_list)+1):
        for j in range(1, len(price_list)+1):
            if i+j <= purchase:
                dp[i+j-1] = max(dp[i+j-1], dp[i-1]+dp[j-1])
    return dp[purchase-1]
