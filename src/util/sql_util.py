import pandas as pd

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

def sql_table_print(cursor, table_name): print(cursor.execute(f"SELECT * FROM {table_name}").fetchall())

def sql_change_print(connection): print(f"(total connection changes)=>{connection.total_changes}", end='\n')

def sql_to_df(connection, table_name) -> pd.DataFrame:
    query = "SELECT * FROM vw_" + table_name
    return pd.read_sql_query(query, connection)


def sql_add_funcs(connection, cursor, func_list):
    """Creates tables using the provided list of creation functions."""
    for create_func in func_list:
        table_name = create_func.__name__.replace('create_', '')
        try:
            create_func(connection, cursor)
        except Exception as e:
            print(f"ERROR: generate_all {table_name}: {e}")
            continue  # Proceed to the next table
