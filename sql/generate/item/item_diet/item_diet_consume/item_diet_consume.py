import sys
import sqlite3
import pandas as pd

from sql.generate.item.item_diet.item_diet_consume.item_diet_consume_list import item_diet_consume_list

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
def sql_table_print(cursor, table_name): print(cursor.execute(f"SELECT * FROM {table_name}").fetchall())

def item_diet_consume_create(connection, cursor):
    # overwrite existing table if it already exists
    sql_table_drop(cursor, "item_diet_consume")

    # create colour table
    cursor.execute('''CREATE TABLE item_diet_consume(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 64)
)''')

    item_diet_consume_list_tuples = [(value,) for value in item_diet_consume_list]

    cursor.executemany("INSERT INTO item_diet_consume(name) VALUES (?)", item_diet_consume_list_tuples)

    cursor.execute("DROP VIEW IF EXISTS vw_item_diet_consume")

    cursor.execute('''
    CREATE VIEW vw_item_diet_consume AS
    SELECT
        idc.id AS id,
        idc.name as name
    FROM item_diet_consume AS idc
''')


    # make changes permanen
    connection.commit()
