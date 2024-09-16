import sys
import sqlite3
import pandas as pd
from sql.utility.sql_table_funcs import sql_table_drop, sql_table_print

from sql.generate.language.name.place_name.place_name_start_list import place_name_start_list

def item_create(connection, cursor):
    table_name = "place_name_start"
    list_name = place_name_start_list

    print("item_create DEBUG")

    # overwrite existing table if it already exists
    sql_table_drop(cursor, table_name)

    # create table
    cursor.execute(f'''CREATE TABLE {table_name} 
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 128),
    item_diet INTEGER NOT NULL,
    colour INTEGER NOT NULL,
    element INTEGER NOT NULL,
    description TEXT NOT NULL CHECK(length(description) <= 128),
    FOREIGN KEY(item_diet) REFERENCES item_diet(id),
    FOREIGN KEY(colour) REFERENCES colour(id),
    FOREIGN KEY(element) REFERENCES element(id)
)''')

    #insert values into table
    cursor.executemany(f"INSERT INTO {table_name}(name, item_diet, colour, element, description) VALUES (?, ?, ?, ?, ?)", list(list_name))

    cursor.execute(f"DROP VIEW IF EXISTS vw_{table_name}")

    cursor.execute(f'''CREATE VIEW vw_{table_name} AS
    SELECT
        tn.id AS id,
        tn.name AS name,
        id.id AS did,
        id.name as diet,
        c.id AS cid,
        c.name AS colour,
        e.id AS eid,
        e.name as element,
        tn.description AS description
    FROM {table_name} AS tn
    INNER JOIN colour AS c ON tn.colour = c.id
    INNER JOIN element AS e ON tn.element = e.id
    INNER JOIN item_diet AS id on tn.item_diet = id.id
    ''')

    # make changes permanent
    connection.commit()
