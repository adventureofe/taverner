import sys
import sqlite3
import pandas as pd
from sql.utility.sql_table_funcs import sql_table_drop, sql_table_print

from sql.generate.move.move_list import move_list

def move_create(connection, cursor):
    table_name = "move"
    list_name = move_list

    # overwrite existing table if it already exists
    sql_table_drop(cursor, table_name)

    # create table
    cursor.execute(f'''CREATE TABLE {table_name}
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 128),
    power INTEGER NOT NULL,
    element INTEGER NOT NULL,
    type INTEGER NOT NULL,
    category INTEGER NOT NULL,
    priority INTEGER NOT NULL,
    description TEXT NOT NULL CHECK(length(description) <= 128),
    FOREIGN KEY(element) REFERENCES element(id),
    FOREIGN KEY(type) REFERENCES move_type(id),
    FOREIGN KEY(category) REFERENCES move_category(id)
)''')

    #insert values into table
    cursor.executemany(f"INSERT INTO {table_name}(name, power, element, type, category, priority, description) VALUES (?, ?, ?, ?, ?, ?, ?)", list(list_name))

    #overwrite existing table if it already exists
    cursor.execute(f'DROP VIEW IF EXISTS vw_{table_name}')

    #create view for table
    cursor.execute(f'''
    CREATE VIEW vw_{table_name} AS
    SELECT
        tn.id AS id,
        tn.name AS name,
        tn.power AS power,
        e.id AS eid,
        e.name as element,
        mt.id AS mtid,
        mt.name as move_type,
        mc.id AS mcid,
        mc.name AS move_category,
        tn.priority AS priority,
        tn.description AS description
        
    FROM {table_name} AS tn
    INNER JOIN element AS e on tn.element = e.id
    INNER JOIN move_type AS mt on tn.type = mt.id
    INNER JOIN move_category AS mc on tn.category = mc.id
''')

    # make changes permanent
    connection.commit()
