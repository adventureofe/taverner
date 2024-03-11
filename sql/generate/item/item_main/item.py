import sys
import sqlite3
import pandas as pd

from sql.generate.item.item_main.item_list import item_list

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
    description TEXT NOT NULL CHECK(length(description) <= 128),
    FOREIGN KEY(item_diet) REFERENCES item_diet(id),
    FOREIGN key(colour) REFERENCES colour(id)
)''')

    #insert values into table
    cursor.executemany("INSERT INTO item(name, item_diet, colour, description) VALUES (?, ?, ?, ?)", list(item_list))

    cursor.execute("DROP VIEW IF EXISTS vw_item")

    cursor.execute('''CREATE VIEW vw_item AS
    SELECT
        i.id AS id,
        i.name AS name,
        id.name AS diet,
        c.name AS colour,
        i.description AS description
    FROM item AS i
    INNER JOIN colour AS c ON i.colour = c.id
    INNER JOIN item_diet AS id on i.item_diet = id.id
    ''')

    # make changes permanent
    connection.commit()
