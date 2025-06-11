import sys
import sqlite3
import pandas as pd
from src.sql.sql_table import SQLTable
from src.sql.sql_table import Config

from src.sql.colour.colour_list import colour_list as values

def colour_base_relation_create(connection, cursor, name="colour_base_relation", values=values):
    print(Config.id)
    table = SQLTable(
        name=name,

        columns=[
            "colour_id INTEGER NOT NULL",
            "base_id INTEGER NOT NULL",
            "PRIMARY KEY (colour_id, base_id)"
        ],

        foreign_keys=[
            "FOREIGN KEY (colour_id) REFERENCES colour(id)",
            "FOREIGN KEY (base_id) REFERENCS colour_base(id)"
        ],

        values=values,

        view_query=f'''
        SELECT
        t.id AS id

        t.colour_id AS c,
        c.name AS colour,

        t.base_id AS b,
        b.name AS base

        FROM {name} AS t


        INNER JOIN colour AS c ON t.colour_id = c.id;
        INNER JOIN colour_base AS b ON t.base_id = b.id;
        ''',
        insert_query=f"INSERT INTO {name} (colour_id, base_id) VALUES (?, ?)"
    )

    table.create(connection, cursor)
    table.change_print(connection, cursor)
    return table
