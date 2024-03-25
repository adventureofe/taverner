import sys
import sqlite3
import pandas as pd


from sql.generate.colour.colour_list import colour_list

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")


def move_create(connection, cursor):
    table_name = "move"

    # overwrite existing table if it already exists
    sql_table_drop(cursor, table_name)

    # create table
    cursor.execute(f'''CREATE TABLE {table_name}
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    power INTEGER NOT NULL,
)''')

    #insert values into table
    cursor.executemany(f"INSERT INTO {table_name}(name, power) VALUES (?, ?)", list(colour_list))

    #overwrite existing table if it already exists
    cursor.execute(f'DROP VIEW IF EXISTS vw_{table_name}')

    #create view for table
    cursor.execute(f'''
    CREATE VIEW vw_{table_name} AS
    SELECT
        tn.id AS id,
        tn.name AS name,
        tn.power AS power
    FROM {table_name} AS tn;
''')

    # make changes permanent
    connection.commit()
