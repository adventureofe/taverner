import sys
import sqlite3
import pandas as pd


from sql.generate.element.element_effectivness.element_effectiveness_type.element_effectiveness_type_list import element_effectiveness_type_list 

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

def element_effectiveness_type_create(connection, cursor):
    # overwrite existing table if it already exists
    sql_table_drop(cursor, "element_effectiveness_type")

    # create table
    cursor.execute('''CREATE TABLE element_effectiveness_type")
    (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
    )''')

    element_effectiveness_type_list_tuples = [(value,) for value in element_effectivesness_type_list]

    cursor.executemany("INSERT INTO element_effectiveness_type(name) VALUES (?)", element_effectectiveness_type_list_tuples)

    #overwrite existing table if it already exists
    cursor.execute('DROP VIEW IF EXISTS vw_element_effectiveness_type')

    #create view for table
    cursor.execute('''
    CREATE VIEW vw_element_effectinvess_type AS
    SELECT
    e.id AS id,
    e.name AS name,
    FROM element_effectiveness_type AS e;
    ''')

    # make changes permanent
    connection.commit()
