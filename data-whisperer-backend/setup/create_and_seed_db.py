import sqlite3

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


def insert_data(conn, table, data):
    try:
        cursor = conn.cursor()
        cursor.executemany(f"INSERT INTO {table} (id, name) VALUES (?, ?)", data)
        conn.commit()
        print(f"{cursor.rowcount} rows inserted.")
    except Exception as e:
        print(e)


def main():
    database = "../sqlite_db/my_database.db"

    sql_create_table = """CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL
                          );"""

    data = [
        (1, 'Alice'),
        (2, 'Bob'),
        (3, 'Charlie'),
    ]

    # Create a connection to the SQLite database
    conn = create_connection(database)

    if conn is not None:
        # Create the 'users' table
        create_table(conn, sql_create_table)

        # Insert sample data
        insert_data(conn, 'users', data)
    else:
        print("Error! Cannot create the database connection.")


if __name__ == '__main__':
    main()
