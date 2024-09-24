import sys
import sqlite3
import pandas as pd
from sql.utility.sql_table_funcs import sql_table_drop, sql_table_print

from sql.generate.element.element_effectiveness.element_effectiveness_type.element_effectiveness_type_list import element_effectiveness_type_list 

def element_effectiveness_type_create(connection, cursor):
    table_name = "element_effectiveness_type"
    list_name = element_effectiveness_type_list

    # overwrite existing table if it already exists
    sql_table_drop(cursor, table_name)

    # create table
    cursor.execute(f'''CREATE TABLE {table_name}
    (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 64),
    level INTEGER NOT NULL,
    multiplier INTEGER NOT NULL
    )''')

    cursor.executemany(f"INSERT INTO {table_name}(name, level, multiplier) VALUES (?, ?, ?)", list_name)



    #overwrite existing table if it already exists
    cursor.execute(f'DROP VIEW IF EXISTS vw_{table_name}')

    #create view for table
    cursor.execute(f'''
    CREATE VIEW vw_{table_name} AS
    SELECT
    tn.id AS id,
    tn.level AS level,
    tn.name AS name,
    tn.multiplier as mult
    FROM {table_name} AS tn;
    ''')

    # make changes permanent
    connection.commit()
