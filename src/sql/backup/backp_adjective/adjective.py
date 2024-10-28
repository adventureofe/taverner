import sys
import sqlite3
import pandas as pd
from src.sql.sql_table import SQLTable

from src.sql.colour.colour_list import adjective_list

def adjective_create(connection, cursor, name="adjective", values=adjective_list):
    table = SQLTable(
        name=name

        columns=[
            "id INTEGER PRIMARY KEY AUTOINCREMENT",
            "name TEXT NOT NULL CHECK(length(name) <= 128)",
            "connotation INTEGER NOT NULL",
       ],

        foreign_keys=[
            "FOREIGN KEY (connotation) REFERENCES adjective_connotation(id)"
        ],

        values=values,

        view_query=f'''
        SELECT
        t.id AS id,
        t.name AS name,
        ac.id AS cid,
        ac.name AS connotation
        FROM {name} AS t
        INNER JOIN adjective_connotation AS ac ON t.connotation = ac.id
        ''',
        insert_query="INSERT INTO colour (name, r, g, b, darkness) VALUES (?, ?, ?, ?, ?)"

    )

    table.create(connection, cursor)
    table.change_print(connection, cursor)
    return table
