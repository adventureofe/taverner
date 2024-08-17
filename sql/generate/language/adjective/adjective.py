import sys
import sqlite3
import pandas as pd

from sql.generate.language.adjective.adjective_list import adjective_list

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
def sql_table_print(cursor, table_name): print(cursor.execute(f"SELECT * FROM {table_name}").fetchall())

def adjective_create(connection, cursor):
    table_name = "adjective"
    list_name = adjective_list
    
    # overwrite existing table if it already exists
    sql_table_drop(cursor, table_name)

    # create table
    cursor.execute(f'''CREATE TABLE {table_name} 
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 128),
    connotation INTEGER NOT NULL,
    FOREIGN KEY (connotation) REFERENCES adjective_connotation(id)
)''')

    #insert values into table
    cursor.executemany(f"INSERT INTO {table_name}(name, connotation) VALUES (?, ?)", list(list_name))

    cursor.execute(f"DROP VIEW IF EXISTS vw_{table_name}")

    cursor.execute(f'''CREATE VIEW vw_{table_name} AS
    SELECT
        tn.id AS id,
        tn.name AS name,
        c.id AS cid,
        c.name AS connotation 
    FROM {table_name} AS tn
    INNER JOIN adjective_connotation AS c ON tn.connotation = c.id
    ''')

    # make changes permanent
    connection.commit()
