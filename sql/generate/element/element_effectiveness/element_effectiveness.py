import sys
import sqlite3
import pandas as pd


from sql.generate.element.element_effectiveness.element_effectiveness_list import element_effectiveness_list

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

def element_effectiveness_create(connection, cursor):
    # overwrite existing table if it already exists
    sql_table_drop(cursor, "element_effectiveness")

    # create table
    cursor.execute('''CREATE TABLE element_effectiveness
    (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    r INTEGER NOT NULL CHECK(r >= 0 AND r <= 255),
    g INTEGER NOT NULL CHECK(g >= 0 AND g <= 255),
    b INTEGER NOT NULL CHECK(b >= 0 AND b <= 255)
    )''')

    #insert values into table
    cursor.executemany("INSERT INTO element_effectivness(name, r, g, b) VALUES (?, ?, ?, ?)", list(element_effectiveness_list))

    #overwrite existing table if it already exists
    cursor.execute('DROP VIEW IF EXISTS vw_element_effectiveness')

    #create view for table
    cursor.execute('''
    CREATE VIEW vw_element_effectiveness AS
    SELECT
    c.id AS id,
    c.name AS name,
    c.r AS r,
    c.g AS g,
    c.b AS b
    FROM element_effectiveness AS c;
    ''')

    # make changes permanent
    connection.commit()
