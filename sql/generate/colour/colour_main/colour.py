import sys
import sqlite3
import pandas as pd


from sql.generate.colour.colour_main.colour_list import colour_list

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

def colour_create(connection, cursor):
    # overwrite existing table if it already exists
    sql_table_drop(cursor, "colour")

    # create table
    cursor.execute('''CREATE TABLE colour
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    r INTEGER NOT NULL CHECK(r >= 0 AND r <= 255),
    g INTEGER NOT NULL CHECK(g >= 0 AND g <= 255),
    b INTEGER NOT NULL CHECK(b >= 0 AND b <= 255)
)''')

    #insert values into table
    cursor.executemany("INSERT INTO colour(name, r, g, b) VALUES (?, ?, ?, ?)", list(colour_list))

    #overwrite existing table if it already exists
    cursor.execute('DROP VIEW IF EXISTS vw_colour')

    #create view for table
    cursor.execute('''
    CREATE VIEW vw_colour AS
    SELECT
        c.id AS id,
        c.name AS name,
        c.r AS r,
        c.g AS g,
        c.b AS b
    FROM colour AS c;
''')

    # make changes permanent
    connection.commit()
