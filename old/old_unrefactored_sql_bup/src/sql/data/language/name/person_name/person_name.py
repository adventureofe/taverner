import sys
import sqlite3
import pandas as pd
from sql.utility.sql_table_funcs import sql_table_drop, sql_table_print

from sql.generate.language.name.person_name.person_name_list import person_name_list

def person_name_create(connection, cursor):
    table_name = "person_name"
    list_name = person_name_list

    # overwrite existing table if it already exists
    sql_table_drop(cursor, table_name)

    # create table
    cursor.execute(f'''CREATE TABLE {table_name} 
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 128),
    gender INTEGER NOT NULL,
    category INTEGER NOT NULL,
    FOREIGN KEY(gender) REFERENCES person_name_gender(id),
    FOREIGN KEY(category) REFERENCES person_name_category(id)
)''')

    #insert values into table
    cursor.executemany(f"INSERT INTO {table_name}(name, gender, category) VALUES (?, ?, ?)", list(list_name))

    cursor.execute(f"DROP VIEW IF EXISTS vw_{table_name}")

    cursor.execute(f'''CREATE VIEW vw_{table_name} AS
    SELECT
        tn.id AS id,
        tn.name AS name,
        psg.id AS gid,
        psg.name AS gender,
        pnc.id AS cid,
        pnc.name as category
    FROM {table_name} AS tn
    INNER JOIN person_name_gender AS psg ON tn.gender= psg.id
    INNER JOIN person_name_category AS pnc ON tn.category = pnc.id
    ''')

    # make changes permanent
    connection.commit()
