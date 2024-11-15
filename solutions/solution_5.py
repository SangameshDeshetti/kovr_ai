# ToDo: Edge cases and exception handling
from utils.orders import orders


def filter_by_status(orders_lst: list, status: str) -> list:
    if not orders_lst:
        return []
    return list(filter(lambda x: x['status'] == status, orders_lst))


def total_revenue_per_customer(orders_list: list) -> dict:
    revenue_per_customer = dict()
    for order in orders_list:
        customer, total = order['customer'], int(order['total'])
        if customer not in revenue_per_customer:
            revenue_per_customer[customer] = total
        else:
            revenue_per_customer[customer] += total
    return revenue_per_customer


if __name__ == '__main__':
    print(filter_by_status(orders, status='pending'))
    print(total_revenue_per_customer(orders))
