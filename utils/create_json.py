import json
import os
import random
from datetime import datetime

from dotenv import load_dotenv
from faker import Faker

load_dotenv()  # Load environment variables from .env file.
START_DATE = os.getenv('START_DATE', datetime.now().date())
START_DATE = datetime.strptime(START_DATE, "%Y-%m-%d")
FILE_NAME = os.getenv('FILE_NAME', 'input.json')

faker = Faker()  # For fake data generation


def generate_column(cols: list):
    column = dict()
    try:
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
    except Exception as e:
        raise e
    finally:
        return column


def create_json(columns: list, num_rows: int):
    data = []
    for _ in range(num_rows):
        column = generate_column(columns)
        data.append(column)

    with open(FILE_NAME, 'w+') as json_file:
        # FILE_NAME is taken from .env file
        json_file.write(json.dumps(data))


if __name__ == '__main__':
    pass
