# ToDo: Edge cases and exception handling
import json
import os
from datetime import datetime

from dotenv import load_dotenv

from utils.create_json import create_json

load_dotenv()  # take environment variables from .env file.
NUM_ROWS = int(os.getenv('NUM_ROWS', 10))
COLUMNS = eval(os.getenv('FIELDS', []))
FILE_NAME = os.getenv('FILE_NAME', 'input.json')


def read_json_from_file():
    with open(FILE_NAME, 'r') as file:
        data = file.readline()
        data = json.loads(data)
        return data


def sales_per_product(sales: list) -> dict:
    product_sales = {}
    for sale in sales:
        product_id = sale["product_id"]
        quantity = int(sale["quantity"])
        price = float(sale["price"])
        revenue = round(quantity * price)

        if product_id not in product_sales:
            product_sales[product_id] = revenue
        else:
            product_sales[product_id] += revenue

    return product_sales


def best_seller(sales: list, input_date: str) -> dict:
    """
    returns product ID and total revenue for that month
    """
    products_in_input_month = {}
    given_date = datetime.strptime(input_date, "%Y-%m")

    for sale in sales:
        sale_date = sale["date"]
        product_id = sale["product_id"]
        quantity = int(sale["quantity"])
        price = float(sale["price"])
        revenue = round(quantity * price)

        sale_date = datetime.strptime(sale_date, "%Y-%m-%d")
        if given_date.date().year == sale_date.date().year and given_date.date().month == sale_date.date().month:
            if product_id not in products_in_input_month:
                products_in_input_month[product_id] = revenue
            else:
                products_in_input_month[product_id] += revenue

        best_seller_product, max_revenue = None, 0

        for key, val in products_in_input_month.items():
            if val > max_revenue:
                best_seller_product, max_revenue = key, val

        return {
            best_seller_product: max_revenue
        }


if __name__ == '__main__':
    # Below line creates a new file each time: name of file is taken from .env file
    create_json(COLUMNS, NUM_ROWS)  # Create the JSON file to work with
    sales_data = read_json_from_file()
    print(sales_per_product(sales_data))
    print(best_seller(sales_data, '2024-03'))
