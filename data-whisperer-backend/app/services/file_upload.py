import sqlite3
from sqlite3 import Error
import pandas as pd

def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
    except Error as err:
        print(err)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as err:
        print(err)

def insert_data(conn, table_name, df):
    # Insert data from the DataFrame into the SQLite table
    df.to_sql(table_name, conn, if_exists='append', index=False)

def create_and_load_table(file_path, database, table_name):
    # Read the file into a DataFrame and infer the schema
    df = pd.read_csv(file_path)
    schema = df.dtypes.to_dict()

    # Generate CREATE TABLE statement
    create_table_statement = f"CREATE TABLE IF NOT EXISTS {table_name} ("

    for column, dtype in schema.items():
        if str(dtype) == 'object':
            sql_type = 'TEXT'
        elif str(dtype).startswith('int'):
            sql_type = 'INTEGER'
        elif str(dtype).startswith('float'):
            sql_type = 'REAL'
        else:
            sql_type = 'TEXT'

        create_table_statement += f"{column} {sql_type}, "

    create_table_statement = create_table_statement.rstrip(", ") + ");"

    # Connect to the SQLite database and create the table
    conn = create_connection(database)
    create_table(conn, create_table_statement)

    # Insert data from the DataFrame into the SQLite table
    insert_data(conn, table_name, df)

    # Close the connection
    conn.close()
