# ToDo: Edge cases and exception handling
import json
import os
from dotenv import load_dotenv
from utils.create_json import create_json

load_dotenv()  # take environment variables from .env file.
NUM_ROWS = int(os.getenv('NUM_ROWS', 10))
COLUMNS = eval(os.getenv('FIELDS', []))
FILE_NAME = os.getenv('FILE_NAME', 'input.json')


"""
    Data Parsing and Aggregation:
    -----------------------------
    You are given a JSON file containing sales data for an e-commerce platform with the following format:
    
    [ {"product_id": "p001", "date": "2023-11-01", "quantity": 2, "price": 20.5},
        {"product_id": "p002", "date": "2023-11-01", "quantity": 1, "price": 50.0}, ... ]
    Each entry represents a sale, including:
    product_id: Unique ID of the product 
    date: Date of the sale in YYYY-MM-DD format 
    quantity: Quantity sold
    price: Price per unit 
    
    Compute Total Sales per Product: 
    Write a function to parse this data and calculate the total revenue generated for each product. 
    The output should be a dictionary with product_id as keys and total revenue as values.
    
    Find the Best-Selling Product of the Month:
    Write a function to identify the product with the highest total revenue within a given month. Your function should 
    take a list of sales records and the month (e.g., "2023-11") as input and return the product ID and revenue.
"""

def read_json_from_file():
    with open(FILE_NAME, 'r') as file:
        data = file.readline()
        data = json.loads(data)
        return data

def sales_per_product(data: list):
    pass

def best_seller():
    pass

if __name__ == '__main__':
    create_json(COLUMNS, NUM_ROWS)  # Create the JSON file to work with
    json_data = read_json_from_file()
    print(sales_per_product())
    print(best_seller())
