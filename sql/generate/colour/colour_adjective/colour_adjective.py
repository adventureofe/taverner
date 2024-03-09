import sys
import sqlite3
import pandas as pd

from sql.generate.colour.colour_adjective.colour_adjective_list import colour_adjective_list

sql_table_drop = lambda cursor, table_name: cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
sql_table_print = lambda cursor, table_name: print(cursor.execute(f"SELECT * FROM {table_name}").fetchall())

def colour_adjective_create(connection, cursor):
    # overwrite existing table if it already exists
    sql_table_drop(cursor, "colour_adjective")

    # create colour table
    cursor.execute('''CREATE TABLE colour_adjective
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)''')

    cursor.executemany("INSERT INTO colour_adjective(name) VALUES(?)", [(name,) for name in colour_adjective_list])

    # make changes permanent
    connection.commit()
