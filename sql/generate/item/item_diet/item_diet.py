import sys
import sqlite3
import pandas as pd

#from sql.generate.item.item_diet.item_diet_list import item_diet_list


def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
def sql_table_print(cursor, table_name): print(cursor.execute(f"SELECT * FROM {table_name}").fetchall())

def item_diet_create(connection, cursor):
    # overwrite existing table if it already exists
    sql_table_drop(cursor, "item_diet")

    # create colour table
    cursor.execute('''CREATE TABLE item_diet
    (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 64),
    consumability INTEGER NOT NULL
    )''')

    cursor.executemany("INSERT INTO item_diet(name, consumability) VALUES (?, ?)", list(item_diet_list))

    # make changes permanent
    connection.commit()
