import pandas as pd

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

def sql_table_print(cursor, table_name): print(cursor.execute(f"SELECT * FROM {table_name}").fetchall())

def sql_change_print(connection): print(f"(total connection changes)=>{connection.total_changes}", end='\n')

def sql_table_to_df(connection, table_name) -> pd.DataFrame:
    query = "SELECT * FROM vw_" + table_name
    return pd.read_sql_query(query, connection)


def sql_table_add_funcs(connection, cursor, func_list):
    """Creates tables using the provided list of creation functions."""
    for create_func in func_list:
        table_name = create_func.__name__.replace('create_', '')
        try:
            create_func(connection, cursor)
        except Exception as e:
            print(f"ERROR: generate_all {table_name}: {e}")
            continue  # Proceed to the next table


def sql_table_init(cursor, table_name, columns, foreign_keys=None):
    """
    Create a table with the specified columns and foreign keys.

    :param cursor: SQLite cursor object.
    :param table_name: Name of the table to create.
    :param columns: List of column definitions as strings.
    :param foreign_keys: List of foreign key definitions as strings (optional).
    """
    foreign_keys_sql = f", {', '.join(foreign_keys)}" if foreign_keys else ""
    columns_sql = ', '.join(columns)
    cursor.execute(f'''
    CREATE TABLE {table_name}
    (
        {columns_sql}
        {foreign_keys_sql}
    )''')

def sql_table_insert(cursor, table_name, values):
    """
    Insert values into the specified table.

    :param cursor: SQLite cursor object.
    :param table_name: Name of the table to insert data into.
    :param values: List of tuples containing the data to insert.
    """
    placeholders = ', '.join(['?' for _ in values[0]])
    cursor.executemany(f"INSERT INTO {table_name} VALUES ({placeholders})", values)

def sql_table_view_create(cursor, table_name, view_name, view_query):
    """
    Create a view based on a query.

    :param cursor: SQLite cursor object.
    :param table_name: The base table for the view.
    :param view_name: Name of the view.
    :param view_query: SQL query that defines the view.
    """
    sql_table_view_drop(cursor, view_name)
    cursor.execute(f'''
    CREATE VIEW {view_name} AS
    {view_query}
    ''')

def sql_table_create(connection, cursor, table_name, columns, foreign_keys, values, view_query):
    """
    General function to create a table, insert values, and create a view.

    :param connection: SQLite connection object.
    :param cursor: SQLite cursor object.
    :param table_name: Name of the table to create.
    :param columns: List of column definitions as strings.
    :param foreign_keys: List of foreign key definitions as strings (optional).
    :param values: List of tuples containing the data to insert.
    :param view_query: SQL query that defines the view.
    """
    # Drop existing table and view
    sql_table_drop(cursor, table_name)

    # Create table
    sql_table_init(cursor, table_name, columns, foreign_keys)

        # Insert values (only for columns except 'id')
    placeholders = ', '.join(['?' for _ in values[0]])  # Assuming each value is a tuple of length 5
    cursor.executemany(f"INSERT INTO {table_name}(name, r, g, b, darkness) VALUES ({placeholders})", values)

    # Create view for table
    sql_table_view_create(cursor, table_name, f'vw_{table_name}', view_query)

    # Commit changes
    connection.commit()
