def max_profit_sale(prices_list: list) -> int:
    max_profit = 0
    try:
        if not prices_list:
            return 0

        min_price = prices_list[0]
        for price in prices_list:
            if price < min_price:
                min_price = price  # Buy at min price for max profit
                max_profit = 0
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit  # Sell at highest price to make max profit
    except Exception as e:
        raise e
    finally:
        return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit_sale(prices))
