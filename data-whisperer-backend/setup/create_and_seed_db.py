import sqlite3
import csv
from typing import Any

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"SQLite version {sqlite3.version} - Connected to {db_file}")
    except Exception as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except Exception as e:
        print(e)


def infer_data_type(value: str) -> Any:
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value


def insert_data(conn, sql_insert, data_path):
    data = []

    with open(data_path, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)

        for row in csvreader:
            values = tuple(infer_data_type(value) for value in row.values())
            data.append(values)

    try:
        cursor = conn.cursor()
        cursor.executemany(sql_insert, data)
        conn.commit()
        print(f"{cursor.rowcount} rows inserted.")
    except Exception as e:
        print(e)

def main():
    # run this script from root/data-whisperer-backend
    database = "sqlite_db/my_database.db"

    sql_create_customers_table = """CREATE TABLE IF NOT EXISTS customers (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL
                          );"""

    sql_create_orders_table = """CREATE TABLE IF NOT EXISTS orders (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER NOT NULL,
                            order_date TEXT NOT NULL,
                            status TEXT NOT NULL,
                            FOREIGN KEY (user_id) REFERENCES customers (id)
                          );"""

    sql_create_payments_table = """CREATE TABLE IF NOT EXISTS payments (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            order_id INTEGER NOT NULL,
                            payment_method TEXT NOT NULL,
                            amount REAL NOT NULL,
                            FOREIGN KEY (order_id) REFERENCES orders (id)
                          );"""

    sql_create_tables = [
        sql_create_customers_table,
        sql_create_orders_table,
        sql_create_payments_table
    ]

    sql_insert_customerms = "INSERT INTO customers (id, first_name, last_name) VALUES (?, ?, ?)"
    sql_insert_orders = "INSERT INTO orders (id, user_id, order_date, status) VALUES (?, ?, ?, ?)"
    sql_insert_payments = "INSERT INTO payments (id, order_id, payment_method, amount) VALUES (?, ?, ?, ?)"

    customer_data_path = "setup/data/raw_customers.csv"
    order_data_path = "setup/data/raw_orders.csv"
    payment_data_path = "setup/data/raw_payments.csv"

    table_insert_data_touples = [
        (sql_insert_customerms, customer_data_path),
        (sql_insert_orders, order_data_path),
        (sql_insert_payments, payment_data_path)
    ]

    # Create a connection to the SQLite database
    conn = create_connection(database)

    if conn is not None:

        for sql_create_table in sql_create_tables:
            create_table(conn, sql_create_table)

        for sql_insert, data_path in table_insert_data_touples:
            # Insert sample data
            insert_data(conn, sql_insert, data_path)
    else:
        print("Error! Cannot create the database connection.")


if __name__ == '__main__':
    main()
