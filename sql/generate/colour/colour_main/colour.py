import sys
import sqlite3
import pandas as pd

from sql.generate.colour.colour_main.colour_list import colour_list

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

def colour_create(connection, cursor):
    # overwrite existing table if it already exists
    sql_table_drop(cursor, "colour")

    # create colour table
    cursor.execute('''CREATE TABLE colour
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    r INTEGER NOT NULL CHECK(r >= 0 AND r <= 255),
    g INTEGER NOT NULL CHECK(g >= 0 AND g <= 255),
    b INTEGER NOT NULL CHECK(b >= 0 AND b <= 255)
)''')

    cursor.executemany("INSERT INTO colour(name, r, g, b) VALUES (?, ?, ?, ?)", list(colour_list))

    # make changes permanent
    connection.commit()
