import sys
import sqlite3
import pandas as pd

from sql.generate.item.item_list import item_list

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
def sql_table_print(cursor, table_name): print(cursor.execute(f"SELECT * FROM {table_name}").fetchall())

def item_create(connection, cursor):
    # overwrite existing table if it already exists
    sql_table_drop(cursor, "item")

    # create table
    cursor.execute('''CREATE TABLE item
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 64),
    item_diet INTEGER NOT NULL,
    colour INTEGER NOT NULL,
    element INTEGER NOT NULL,
    description TEXT NOT NULL CHECK(length(description) <= 128),
    FOREIGN KEY(item_diet) REFERENCES item_diet(id),
    FOREIGN KEY(colour) REFERENCES colour(id),
    FOREIGN KEY(element) REFERENCES element(id)
)''')

    #insert values into table
    cursor.executemany("INSERT INTO item(name, item_diet, colour, element, description) VALUES (?, ?, ?, ?, ?)", list(item_list))

    cursor.execute("DROP VIEW IF EXISTS vw_item")

    cursor.execute('''CREATE VIEW vw_item AS
    SELECT
        i.id AS id,
        i.name AS name,
        id.id AS did,
        id.name as diet,
        c.id AS cid,
        c.name AS colour,
        e.id AS eid,
        e.name as element,
        i.description AS description
    FROM item AS i
    INNER JOIN colour AS c ON i.colour = c.id
    INNER JOIN element AS e ON i.element = e.id
    INNER JOIN item_diet AS id on i.item_diet = id.id
    ''')

    # make changes permanent
    connection.commit()
