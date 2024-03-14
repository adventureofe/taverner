import sys
import sqlite3
import pandas as pd

from sql.generate.language.adjective.adjective_list import adjective_list

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
def sql_table_print(cursor, table_name): print(cursor.execute(f"SELECT * FROM {table_name}").fetchall())

def item_create(connection, cursor):
    # overwrite existing table if it already exists
    sql_table_drop(cursor, "item")

    # create table
    cursor.execute('''CREATE TABLE adjective
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 64)
)''')

    adjective_list_tuples = [(value,) for value in adjective_list]


    #insert values into table
    cursor.executemany("INSERT INTO item(name) VALUES (?)", adjective_list_tuples)

    cursor.execute("DROP VIEW IF EXISTS vw_adjective")

    cursor.execute('''CREATE VIEW vw_adjective AS
    SELECT
        a.id AS id,
        a.name AS name,
    FROM adjective AS a;
    ''')

    # make changes permanent
    connection.commit()
