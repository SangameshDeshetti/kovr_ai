from utils.orders import orders


def filter_by_status(orders_lst: list, status: str) -> list:
    if not orders_lst:
        return []
    # filter list by status, as per given status.
    return list(filter(lambda x: x['status'] == status, orders_lst))


def total_revenue_per_customer(orders_list: list) -> dict:
    revenue_per_customer = dict()
    try:
        for order in orders_list:
            customer, total = order['customer'], int(order['total'])
            if customer not in revenue_per_customer:
                revenue_per_customer[customer] = total
            else:
                revenue_per_customer[customer] += total
    except Exception as e:
        raise e
    finally:
        return revenue_per_customer


if __name__ == '__main__':
    print(filter_by_status(orders, status='pending'))
    print(total_revenue_per_customer(orders))
