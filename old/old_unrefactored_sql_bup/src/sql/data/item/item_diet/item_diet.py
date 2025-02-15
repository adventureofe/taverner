import sys
import sqlite3
import pandas as pd
from sql.utility.sql_table_funcs import sql_table_drop, sql_table_print

from sql.generate.item.item_diet.item_diet_list import item_diet_list

def item_diet_create(connection, cursor):
    table_name = "item_diet"
    list_name = item_diet_list
    
    # overwrite existing table if it already exists
    sql_table_drop(cursor, table_name) 

    # create colour table
    cursor.execute(f'''CREATE TABLE {table_name}
    (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 128)
    )''')

    item_diet_list_tuples = [(value,) for value in list_name]

    cursor.executemany(f"INSERT INTO {table_name}(name) VALUES (?)", item_diet_list_tuples)

    cursor.execute(f"DROP VIEW IF EXISTS vw_{table_name}")

    cursor.execute(f'''
    CREATE VIEW vw_{table_name} AS
    SELECT
        tn.id AS id,
        tn.name as name
    FROM {table_name} AS tn
''')

    # make changes permanent
    connection.commit()
