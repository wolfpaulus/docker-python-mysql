"""
This module handles database operations for a simple application.
It includes functions to connect to the database, initialize the database,
insert, and fetch all records from the database.
"""
from typing import Optional
import json
import mysql.connector


def connect_db(config: dict) -> Optional[mysql.connector.connection.MySQLConnection]:
    """Establishes and returns a database connection."""
    try:
        return mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None


def initialize_db(config: dict) -> None:
    """Creates the 'numbers' table if it does not exist."""
    if conn := connect_db(config):
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "CREATE TABLE IF NOT EXISTS numbers(id INT AUTO_INCREMENT PRIMARY KEY, values_list JSON NOT NULL);")
                conn.commit()
        except mysql.connector.Error as err:
            print(f"Error initializing database: {err}")
        finally:
            conn.close()


def insert_random_numbers(config: dict, numbers: list[int]) -> None:
    """Inserts 10 random numbers into the database."""
    if conn := connect_db(config):
        try:

            with conn.cursor() as cursor:
                numbers_json = json.dumps(numbers)  # Convert to JSON string
                cursor.execute("INSERT INTO numbers (values_list) VALUES (%s);", (numbers_json,))
                conn.commit()
        except mysql.connector.Error as err:
            print(f"Error inserting data: {err}")
        finally:
            conn.close()


def fetch_numbers(config: dict) -> list[list[int]]:
    """Fetches all records from the numbers table."""
    if conn := connect_db(config):
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT values_list FROM numbers;")
                rows = cursor.fetchall()
                numbers_lists = []
                for row in rows:
                    numbers_lists.append(json.loads(row["values_list"]))  # Convert JSON to Python list
                return numbers_lists
        except mysql.connector.Error as err:
            print(f"Error inserting data: {err}")
            return []
        finally:
            conn.close()
