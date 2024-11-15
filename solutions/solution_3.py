# ToDo: Edge cases and exception handling
def max_profit_sale(prices_list: list) -> int:
    if not prices_list:
        return 0

    max_profit, min_price = 0, prices_list[0]
    for price in prices_list:
        if price < min_price:
            min_price = price
            max_profit = 0
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit

    return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit_sale(prices))
