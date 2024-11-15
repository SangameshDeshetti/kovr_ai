import json
import os
import random
from datetime import datetime

from faker import Faker
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env file.
NUM_ROWS = int(os.getenv('NUM_ROWS', 10))
COLUMNS = eval(os.getenv('FIELDS', []))
START_DATE = os.getenv('START_DATE', datetime.now().date())
START_DATE = datetime.strptime(START_DATE, "%Y-%m-%d")

faker = Faker()  # For fake data generation


def generate_column(cols):
    column = dict()
    for col in cols:
        if col == "product_id":
            column["product_id"] = random.randint(0, 100)
        if col == "date":
            random_date = faker.date_between_dates(START_DATE, datetime.now().date())
            random_date = datetime.strftime(random_date, '%Y-%m-%d')
            column["date"] = random_date
        if col == "quantity":
            column["quantity"] = random.randint(1, 15)
        if col == "price":
            column["price"] = round(random.uniform(1.00, 100.00), 2)
    return column


def create_json(columns, num_rows):
    data = []
    for _ in range(num_rows):
        column = generate_column(columns)
        data.append(column)

    with open("input.json", 'w+') as json_file:
        json_file.write(json.dumps(data))


if __name__ == '__main__':
    create_json(COLUMNS, NUM_ROWS)
