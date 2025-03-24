""" Main application file to generate random numbers and interact with the database. """
from random import randint
from time import sleep
import os
import db_utils


def create_random_numbers(limit=10) -> list[int]:
    """Generate <limit> random numbers between 1 and <limit>."""
    return [randint(1, limit) for _ in range(limit)]


# Allow time for MySQL to initialize
sleep(10)

CONFIG = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", "rootpassword"),
    "database": os.getenv("MYSQL_DATABASE", "demo_db"),
}

if __name__ == "__main__":
    db_utils.initialize_db(CONFIG)
    while True:
        sleep(10)
        print("Generating random numbers and inserting into the database...")
        nums = create_random_numbers(randint(3, 7))
        print(nums)
        db_utils.insert_random_numbers(CONFIG, nums)
        print("Inserted into the database.")
