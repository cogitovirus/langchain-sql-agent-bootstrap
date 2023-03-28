import pandas as pd
from sqlalchemy import text

def create_table(db, create_table_sql):
    try:
        db.engine.execute(text(create_table_sql))
    except Exception as err:
        print(err)

def insert_data(db, table_name, df):
    # Insert data from the DataFrame into the SQLite table
    df.to_sql(table_name, db.engine, if_exists='append', index=False)

def create_and_load_table(file_path, db, table_name):
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

    # Create the table
    create_table(db, create_table_statement)

    # Insert data from the DataFrame into the SQLite table
    insert_data(db, table_name, df)
