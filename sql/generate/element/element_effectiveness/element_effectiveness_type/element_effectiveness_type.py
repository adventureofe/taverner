import sys
import sqlite3
import pandas as pd

from sql.generate.element.element_effectiveness.element_effectiveness_type.element_effectiveness_type_list import element_effectiveness_type_list 

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

def element_effectiveness_type_create(connection, cursor):
    # overwrite existing table if it already exists
    sql_table_drop(cursor, "element_effectiveness_type")

    # create table
    cursor.execute('''CREATE TABLE element_effectiveness_type
    (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 64),
    multiplier FLOAT NOT NULL
    )''')

    cursor.executemany("INSERT INTO element_effectiveness_type(name, multiplier) VALUES (?, ?)", element_effectiveness_type_list)



    #overwrite existing table if it already exists
    cursor.execute('DROP VIEW IF EXISTS vw_element_effectiveness_type')

    #create view for table
    cursor.execute('''
    CREATE VIEW vw_element_effectiveness_type AS
    SELECT
    e.id AS id,
    e.name AS name,
    e.multiplier as mult
    FROM element_effectiveness_type AS e;
    ''')

    # make changes permanent
    connection.commit()
