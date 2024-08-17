import sys
import sqlite3
import pandas as pd


from sql.generate.colour.colour_list import colour_list

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

def colour_create(connection, cursor):
    table_name = "colour"
    list_name = colour_list

    # overwrite existing table if it already exists
    sql_table_drop(cursor, table_name)

    # create table
    cursor.execute(f'''CREATE TABLE {table_name} 
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 128),
    r INTEGER NOT NULL CHECK(r >= 0 AND r <= 255),
    g INTEGER NOT NULL CHECK(g >= 0 AND g <= 255),
    b INTEGER NOT NULL CHECK(b >= 0 AND b <= 255)
)''')

    #insert values into table
    cursor.executemany(f"INSERT INTO {table_name}(name, r, g, b) VALUES (?, ?, ?, ?)", list(list_name))

    #overwrite existing table if it already exists
    cursor.execute(f'DROP VIEW IF EXISTS vw_{table_name}')

    #create view for table
    cursor.execute(f'''
    CREATE VIEW vw_{table_name} AS
    SELECT
        tn.id AS id,
        tn.name AS name,
        tn.r AS r,
        tn.g AS g,
        tn.b AS b
    FROM {table_name} AS tn;
''')

    # make changes permanent
    connection.commit()
