import pandas as pd

from dataclasses import dataclass
from typing import List, Tuple, Optional

@dataclass
class SQLTable:
    name: str
    columns: List[str]
    foreign_keys: List[str]
    values: List[Tuple]
    view_query: str

    def drop(self, cursor):
        cursor.execute(f"DROP TABLE IF EXISTS {self.table_name}")

    def print(self, cursor):
        rows = cursor.execute(f"SELECT * FROM {self.table_name}").fetchall()
        print(rows)

   def change_print(self, connection):
        """Print total connection changes."""
        print(f"(total connection changes)=>{connection.total_changes}")


def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

def sql_table_print(cursor, table_name): print(cursor.execute(f"SELECT * FROM {table_name}").fetchall())

def sql_change_print(connection): print(f"(total connection changes)=>{connection.total_changes}", end='\n')

def sql_table_to_df(connection, table_name) -> pd.DataFrame:
    query = "SELECT * FROM vw_" + table_name
    return pd.read_sql_query(query, connection)


def sql_table_add_funcs(connection, cursor, func_list):
    for create_func in func_list:
        table_name = create_func.__name__.replace('create_', '')
        try:
            create_func(connection, cursor)
        except Exception as e:
            print(f"ERROR: generate_all {table_name}: {e}")
            continue  # Proceed to the next table


def sql_table_init(cursor, table_name, columns, foreign_keys=None):
    foreign_keys_sql = f", {', '.join(foreign_keys)}" if foreign_keys else ""
    columns_sql = ', '.join(columns)
    cursor.execute(f'''
    CREATE TABLE {table_name}
    (
        {columns_sql}
        {foreign_keys_sql}
    )''')

def sql_table_insert(cursor, table_name, values):
    placeholders = ', '.join(['?' for _ in values[0]])
    cursor.executemany(f"INSERT INTO {table_name} VALUES ({placeholders})", values)

def sql_table_view_create(cursor, table_name, view_query):
    sql_table_view_drop(cursor, table_name)
    cursor.execute(f'''
    CREATE VIEW vw_{table_name} AS
    {view_query}
    ''')

def sql_table_view_drop(cursor, table_name):
    cursor.execute(f"DROP VIEW IF EXISTS vw_{table_name}")

def sql_table_create(connection, cursor, table: SQLTable):
    sql_table_drop(cursor, table.table_name)
    sql_table_view_drop(cursor, table.table_name)

    sql_table_init(cursor, table.table_name, table.columns, table.foreign_keys)

    # Insert values (only for columns except 'id')
    placeholders = ', '.join(['?' for _ in values[0]])  # Assuming each value is a tuple of length 5
    cursor.executemany(f"INSERT INTO {table.table_name}(name, r, g, b, darkness) VALUES ({placeholders})", values)

    # Create view for table
    sql_table_view_create(cursor, table.table_name, table.view_query)

    # Commit changes
    connection.commit()
