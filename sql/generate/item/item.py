import sys
import sqlite3
import pandas as pd

from sql.generate.item.item_list import item_list

sql_table_drop = lambda cursor, table_name: cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
sql_table_print = lambda cursor, table_name: print(cursor.execute(f"SELECT * FROM {table_name}").fetchall())

def item_create(connection, cursor):
    # overwrite existing table if it already exists
    sql_table_drop(cursor, "item")

    # create colour table
    cursor.execute('''CREATE TABLE item
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 64),
    diet INTEGER NOT NULL,
    colour INTEGER NOT NULL,
    description TEXT NOT NULL CHECK(length(description) <= 128),
    FOREIGN KEY(diet) REFERENCES item_diet(id),
    FOREIGN key(colour) REFERENCES colour(id)
)''')

    cursor.executemany("INSERT INTO colour(name, r, g, b) VALUES (?, ?, ?, ?)", list(colour_list))

    # make changes permanent
    connection.commit()
